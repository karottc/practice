﻿#include <sys/socket.h>
#include <sys/wait.h>
#include <netinet/in.h>
#include <netinet/tcp.h>
#include <sys/epoll.h>
#include <sys/sendfile.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <fcntl.h>
#include <errno.h>

#include <iostream>

using namespace std;

#define LOGINFO cout << __FUNCTION__ << ":" << __LINE__

// 最大支持1000的并发
#define MAX_EVENTS 1000
#define PORT 8090

//设置socket连接为非阻塞模式
void setnonblocking(int sockfd) {
    int opts;
    opts = fcntl(sockfd, F_GETFL);
    if(opts < 0) {
        LOGINFO << ": fcntl(F_GETFL)\n" << endl;
        exit(1);
    }
    opts = (opts | O_NONBLOCK);
    if(fcntl(sockfd, F_SETFL, opts) < 0) {
        LOGINFO << ": fcntl(F_SETFL)\n" << endl;
        exit(1);
    }
}

int main(){
    struct epoll_event ev; //ev负责添加事件，events接收返回事件
    int addrlen, listenfd, conn_sock, nfds, epfd, fd, i, nread, n;
    struct sockaddr_in local, remote;

    //创建listen socket
    if( (listenfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("sockfd\n");
        exit(1);
    }
    // 对方关闭链接会抛出SIGPIPE异常，屏蔽掉
    signal(SIGPIPE, SIG_IGN);
    setnonblocking(listenfd);//listenfd设置为非阻塞[1]
    bzero(&local, sizeof(local));
    local.sin_family = AF_INET;
    local.sin_addr.s_addr = htonl(INADDR_ANY);
    local.sin_port = htons(PORT);
    if( bind(listenfd, (struct sockaddr *) &local, sizeof(local)) < 0) {
        perror("bind\n");
        exit(1);
    }
    // 后面这个值的上限一般是128
    listen(listenfd, 20);

    epfd = epoll_create(MAX_EVENTS);
    if (epfd == -1) {
        LOGINFO << ": epoll_create failed." << endl;
        exit(EXIT_FAILURE);
    }

    ev.events = EPOLLIN | EPOLLET;
    ev.data.fd = listenfd;
    LOGINFO << ": add fd=" << listenfd << " listen" << endl;
    if (epoll_ctl(epfd, EPOLL_CTL_ADD, listenfd, &ev) == -1) {//监听listenfd
        LOGINFO << ": epoll_ctl: listen_sock failed" << endl;
        exit(EXIT_FAILURE);
    }

    int shRet = 0;
    uint32_t times = 0;
    while(1) {
        struct epoll_event events[MAX_EVENTS];
        times++;
        nfds = epoll_wait(epfd, events, MAX_EVENTS, -1);
        if (nfds == -1) {
            LOGINFO << "epoll_pwait failed" << endl;
            exit(EXIT_FAILURE);
        }

        LOGINFO << ": readynum=" << nfds << endl;

        for (i = 0; i < nfds; ++i) {
            fd = events[i].data.fd;
            if (fd == listenfd) {
                while ((conn_sock = accept(listenfd,(struct sockaddr *) &remote, 
                                (socklen_t *)&addrlen)) > 0) {
                    setnonblocking(conn_sock);//下面设置ET模式，所以要设置非阻塞
                    ev.events = EPOLLIN | EPOLLET;
                    ev.data.fd = conn_sock;
                    LOGINFO << ": add fd=" << conn_sock << ", connectfd" << endl;
                    if (epoll_ctl(epfd, EPOLL_CTL_ADD, conn_sock, &ev) == -1) {//读监听
                        LOGINFO << ": epoll_ctl: add failed" << endl; //连接套接字
                        exit(EXIT_FAILURE);
                    }
                }
                if (conn_sock == -1) {
                    if (errno != EAGAIN && errno != ECONNABORTED 
                            && errno != EPROTO && errno != EINTR) 
                        LOGINFO << ": accept" << endl;
                }
                continue;
            } 
            if (events[i].events & EPOLLIN) {
                char buf[BUFSIZ];
                memset(buf, 0, BUFSIZ);
                n = 0;
                while ((nread = read(fd, buf + n, BUFSIZ-1)) > 0) {//ET下可以读就一直读
                    n += nread;
                }
                LOGINFO << ": nread=" << nread << ",errno=" << errno << endl;
                if (nread == -1 && errno != EAGAIN) {
                    LOGINFO << ": read error" << endl;
                }
                ev.data.fd = fd;
                //ev.events = events[i].events | EPOLLOUT | EPOLLET; //MOD OUT 
                ev.events = EPOLLOUT | EPOLLET; //MOD OUT 
                LOGINFO << ": mod fd=" << fd << ", epollin" << endl;
                if (epoll_ctl(epfd, EPOLL_CTL_MOD, fd, &ev) == -1) {
                    LOGINFO << ": epoll_ctl: mod failed" << endl;
                }
                LOGINFO << ": n=" << n << ",recv=" << buf << endl;
                LOGINFO << ": shutdown rd" << endl;
                shRet = shutdown(fd, SHUT_RD);
                if (0 != shRet) {
                    LOGINFO << ": shutdown rd error. errno=" << errno << endl;
                }
                //close(fd);
            }
            if (events[i].events & EPOLLOUT) {
                //char buf[100]="1234567890\n1234567890\n";
                char buf[100];
                memset(buf, 0, BUFSIZ);
                cout << "Pleae input: ";
                cin >> buf;
                //close(fd);
                int nwrite, data_size = strlen(buf);
                n = data_size;
                while (n > 0) {
                    nwrite = write(fd, buf + data_size - n, n);//ET下一直将要写数据写完
                    LOGINFO << ": nwrite=" << nwrite << ",errno=" << errno << endl;
                    if (nwrite < n) {
                        if (nwrite == -1 && errno != EAGAIN) {
                            LOGINFO << ":write error" << endl;
                        }
                        break;
                    }
                    n -= nwrite;
                }
                ev.data.fd = fd;
                ev.events = EPOLLIN | EPOLLET; //MOD IN 
                //LOGINFO << ": mod fd=" << fd << ", epollin" << endl;
                if (epoll_ctl(epfd, EPOLL_CTL_MOD, fd, &ev) == -1) {
                    LOGINFO << ": epoll_ctl: mod failed" << endl;
                }
                LOGINFO << ": shutdown wr" << endl;
                //shRet = shutdown(fd, SHUT_WR);
                shRet = close(fd);
                if (0 != shRet) {
                    LOGINFO << ": shutdown wr error. errno=" << errno << endl;
                }
                //close(fd);
            }
        }
    }
    return 0;
}
