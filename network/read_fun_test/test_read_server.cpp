#include <sys/socket.h>
#include <errno.h>
#include <fcntl.h>
#include <netinet/in.h>
#include <netinet/tcp.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <sys/epoll.h>
#include <sys/sendfile.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <unistd.h>

#include <iostream>
#include <string>

using namespace std;

#define LOGINFO cout << "[" << __FILE__ << "|" << __FUNCTION__ << "|" << __LINE__ << "]"

// 最大支持1000的并发
#define MAX_EVENTS 1000
#define PORT 8090

//设置socket连接为非阻塞模式
void setnonblocking(int sockfd) {
    int opts;
    opts = fcntl(sockfd, F_GETFL);
    if (opts < 0) {
        LOGINFO << ": fcntl(F_GETFL)\n" << endl;
        exit(1);
    }
    opts = (opts | O_NONBLOCK);
    if (fcntl(sockfd, F_SETFL, opts) < 0) {
        LOGINFO << ": fcntl(F_SETFL)\n" << endl;
        exit(1);
    }
}

int main()
{
    int addrlen, listenfd;
    struct sockaddr_in local, remote;

    //创建listen socket
    if ((listenfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("sockfd\n");
        exit(1);
    }
    int on = 1;
    setsockopt( listenfd, SOL_SOCKET, SO_REUSEADDR, &on, sizeof(on) );
    // 对方关闭链接会抛出SIGPIPE异常，屏蔽掉
    // signal(SIGPIPE, SIG_IGN);
    // setnonblocking(listenfd);//listenfd设置为非阻塞[1]
    bzero(&local, sizeof(local));
    local.sin_family = AF_INET;
    local.sin_addr.s_addr = htonl(INADDR_ANY);
    local.sin_port = htons(PORT);
    if (bind(listenfd, (struct sockaddr *)&local, sizeof(local)) < 0) {
        perror("bind\n");
        exit(1);
    }
    LOGINFO << "listenfd=" << listenfd << endl;
    // 后面这个值的上限一般是128
    listen(listenfd, 20);

    while (1) {
        struct sockaddr_in client_addr;
        int conn_fd = accept(listenfd, (sockaddr *)&client_addr, (socklen_t *)&addrlen);
        if (conn_fd == -1) {
            LOGINFO << "accept failed|" << errno << endl;
            continue;
        }

        LOGINFO << "conn_fd=" << conn_fd << endl;
        // int ret = close(conn_fd);
        // LOGINFO << "ret=" << ret << endl;
        // setnonblocking(conn_fd);
        int nread = 1;
        while (nread != 0) {
            char buf[20];
            memset(buf, 0, 20);
            int n = 0;
            string tmp = "";
            // close(conn_fd);
            // sleep(20);
            // exit(0);
            while ((nread = read(conn_fd, buf, 20)) >= 20) {
                tmp += buf;
                LOGINFO << "nread=" << nread << ",errno=" << errno << endl;
            }
            tmp += buf;
            LOGINFO << "nread=" << nread << ",errno=" << errno << endl;
            LOGINFO << "content=" << buf << "|" << tmp << endl;

            string input = "";
            // cout << "Please input: ";
            // cin >> input;
            input = tmp;
            if (input == "exit") {
                int ret = close(conn_fd);
                LOGINFO << "ret=" << ret << endl;
                break;
            }
            int nbyte = 0;
            nbyte = write(conn_fd, input.c_str(), input.size());
            if (-1 == nbyte) {
                LOGINFO << " write error. erron=" << errno << endl;
                break;
            }
            LOGINFO << "nbyte=" << nbyte << endl;
            if (nread == 0) {
                int ret = close(conn_fd);
                LOGINFO << "ret=" << ret << endl;
            }
            // exit(0);
        }
    }
    return 0;
}
