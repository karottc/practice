#include <arpa/inet.h>
#include <errno.h>
#include <fcntl.h>
#include <iostream>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <sys/socket.h>
#include <unistd.h>

using namespace std;

#define LOGINFO cout << "[" << __FILE__ << "|" << __FUNCTION__ << "|" << __LINE__ << "]"
#define PORT 8090

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

void set_socket_timeout(int sockfd)
{
    struct timeval ti;
    ti.tv_sec = 3;
    ti.tv_usec = 0;
    int ret = setsockopt(sockfd, SOL_SOCKET,SO_RCVTIMEO, &ti, sizeof(ti));
    LOGINFO << "ret=" << ret << endl;
}


int main(void)
{
    int sockfd;
    int rc;
    int cpid;
    struct sockaddr_in servaddr;

    // signal(SIGPIPE, SIG_IGN);

    bzero(&servaddr, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    inet_pton(AF_INET, "127.0.0.1", &servaddr.sin_addr);
    servaddr.sin_port = htons(PORT);

    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    rc = connect(sockfd, (struct sockaddr *)&servaddr, sizeof(servaddr));
    if (-1 == rc) {
        LOGINFO << ": connect error. " << endl;
        exit(-1);
    }
    // set_socket_timeout(sockfd);
    setnonblocking(sockfd);
    int wn = 0;
    int rn = 0;
    int shRet = 0;
    while (1) {
        cout << endl;
        LOGINFO << ": fd=" << sockfd << endl;
        // char input[1024] = "eeeeeeeeeeeee";
        string input = "";
        cout << "Please input: ";
        cin >> input;
        int nbyte = 0;
        nbyte = write(sockfd, input.c_str(), input.size());
        if (-1 == nbyte) {
            LOGINFO << " write error. erron=" << errno << endl;
            // exit(-1);
            break;
        }
        LOGINFO << "nbyte=" << nbyte << endl;

        if (input == "exit") {
            int ret = close(sockfd);
            LOGINFO << "close ret=" << ret << endl;
            break;
        }

        char buf[20];
        memset(buf, 0, 20);
        int nread = 0;
        string tmp = "";
        while ((nread = read(sockfd,buf,20)) >= 20) {
           tmp += buf;
           LOGINFO << "nread=" << nread << ",errno=" << errno << endl;
        }
        LOGINFO << "nread=" << nread << ",errno=" << errno << endl;
        LOGINFO << "content=" << buf << "|" << tmp << endl;
        if (nread == 0) {
            int ret = close(sockfd);
            LOGINFO << "ret=" << ret << endl;
            break;
        }
    }
    shRet = close(sockfd);
    LOGINFO << "shRet=" << shRet << ",errno=" << errno << endl;

    return 0;
}
