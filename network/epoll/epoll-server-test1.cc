#include <iostream>
#include <unistd.h>
#include <stdlib.h>
#include <sys/epoll.h>
#include <errno.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>
#include <fcntl.h>

using namespace std;

// 设置非阻塞socket
void setnonblocking(int sock)
{
    int opts;
    opts = fcntl(sock, F_GETFL);
    if (opts < 0)
    {
        cerr << "fcntl failed!!" << endl;
        exit(1);
    }
    opts = opts | O_NONBLOCK;
    if (fcntl(sock, F_SETFL, opts) < 0)
    {
        cerr << "nonblocking failed !!" << endl;
        exit(1);
    }
}


int main(int argc, char** argv)
{
    const int MAXLINE = 20;
    const int LISTENQ = 20;
    int portnumber;    // 服务器监听的端口号
    int listenfd, connfd, sockfd;
    socklen_t clilen;
    char line[MAXLINE];
    int epfd, nfds, n;
    // ev用于注册事件，events用于回传要处理的事件
    struct epoll_event ev, events[5];

    if ( 2 == argc )
    {
        if ( (portnumber = atoi(argv[1])) < 0 )
        {
            cerr << "Usage: " << argv[0] << " portnumber" << endl;
            return 1;
        }
    }
    else
    {
        cerr << "Usage: " << argv[0] << " portnumber" << endl;
        return 1;
    }

    epfd = epoll_create(1);
    struct sockaddr_in clientaddr;
    struct sockaddr_in serveraddr;
    
    listenfd = socket(AF_INET,SOCK_STREAM, 0);
    setnonblocking(listenfd);
    
    ev.data.fd = listenfd;          // 设置与要处理事件相关的文件描述符
    ev.events = EPOLLIN | EPOLLET;  // 设置要处理的事件类型。
    epoll_ctl(epfd, EPOLL_CTL_ADD,listenfd, &ev);   // 注册事件
    
    memset(&serveraddr, 0, sizeof(serveraddr));
    serveraddr.sin_family = AF_INET;
    string local_addr = "127.0.0.1";
    inet_aton(local_addr.c_str(), &(serveraddr.sin_addr));
    serveraddr.sin_port = htons(portnumber);
    
    if ( bind(listenfd, (sockaddr *)&serveraddr, sizeof(serveraddr)) )
    {
        cerr << "Bind address " << local_addr << " failed !!" << endl;
        return 1;
    }
    listen(listenfd, LISTENQ);
  
    string output;
    while (1)
    {
        nfds = epoll_wait(epfd,events,5, -1);
        for (int i = 0; i < nfds; ++i)
        {
            cout << "i = " << i << ", nfds = " << nfds << endl;
            // 检测到一个SOCKET用户连接到了绑定的SOCKET端口，建立新连接。
            if (events[i].data.fd == listenfd)
            {
                connfd = accept(listenfd, (sockaddr *)&clientaddr, &clilen);
                if (connfd < 0)
                {
                    cerr << "connfd < 0" << endl;
                    exit(1);
                }
                char *str = inet_ntoa(clientaddr.sin_addr);
                cout << "accept a connection from " << str << endl;
                ev.data.fd = connfd;   // 设置用于读操作的文件描述符
                ev.events = EPOLLIN | EPOLLET;
                epoll_ctl(epfd, EPOLL_CTL_ADD, connfd, &ev);
            }
            else if (events[i].events & EPOLLIN)   // 已经连接的用户，收到数据，读入数据
            {
                cout << "EPOLLIN" << endl;
                if ((sockfd = events[i].data.fd) < 0)
                    continue;
                memset(line,0,sizeof(line));
            
                setnonblocking(sockfd);
                while ((n = read(sockfd, line, MAXLINE)) > 0)
                {
                    //cout << "read(n=" << n << "): "<< line << endl;
                    output += line;
                    memset(line,0,sizeof(line));
                }
                cout << "Output size = " << output.size() << ": " << output << endl;
                output.clear();
                /*
                ev.data.fd = sockfd;    // 设置用于写操作文件描述符
                ev.events = EPOLLOUT|EPOLLET;
                epoll_ctl(epfd, EPOLL_CTL_MOD, sockfd, &ev);
                */
            }
            else if (events[i].events & EPOLLOUT)
            {
                sockfd = events[i].data.fd;
                cout << "Output: " << output << endl;
                output.clear();
                ev.data.fd = sockfd;
                ev.events = EPOLLIN | EPOLLET;
                epoll_ctl(epfd, EPOLL_CTL_MOD, sockfd, &ev);
            }
        }
    }
    return 0;
}
