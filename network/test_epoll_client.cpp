#include <sys/socket.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>
#include <stdlib.h>
#include <signal.h>
#include <errno.h>
#include <fcntl.h>

#include <iostream>
#include <string>

using namespace std;

#define LOGINFO cout << __FUNCTION__ << ":" << __LINE__
#define PORT 8090

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


int main(void)
{
    int sockfd;
    int rc;
    int cpid;
    struct sockaddr_in servaddr;

    signal(SIGPIPE, SIG_IGN);

    bzero(&servaddr, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    inet_pton(AF_INET, "127.0.0.1", &servaddr.sin_addr);
    servaddr.sin_port = htons(PORT);

    /*
    for (int i = 0; i < 20; i++) {
        cpid = fork();
        if (cpid == 0) {
            sockfd = socket(AF_INET, SOCK_STREAM, 0);
            rc = connect(sockfd, (struct sockaddr*)&servaddr, sizeof(servaddr));
            if (-1 == rc) {
                LOGINFO << ": connect error." << endl;
                exit(-1);
            }

            LOGINFO << ": connect. pid=" << getpid() << endl;

            close(sockfd);
            exit(0);
        }
    }
    */
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    rc = connect(sockfd, (struct sockaddr*)&servaddr, sizeof(servaddr));
    if (-1 == rc) {
        LOGINFO << ": connect error. " << endl;
        exit(-1);
    }

    //setnonblocking(sockfd);
    int wn = 0;
    int rn = 0;
    int shRet = 0;
    while (1) {
        cout << endl;
        LOGINFO << ": fd=" << sockfd << endl;
        char input[1024] = "xxxxxx";
        //cout << "Please input: ";
        //cin >> input;
        //input = "xxxxx";
        //close(sockfd);
        int nbyte = 0;
        if (wn == 0) {
            //shutdown(sockfd, SHUT_WR);
            nbyte = write(sockfd, input, strlen(input));
            if (-1 == nbyte) {
                LOGINFO << " write error. erron=" << errno << endl;
                exit(-1);
            }
            wn++;
            LOGINFO << ": shutdown wr." << endl;
            shRet = shutdown(sockfd, SHUT_WR);
            if (0 != shRet) {
                LOGINFO << ": shutdown wr error. errno=" << errno <<endl;
            }
        }

        char recvbuf[1024];
        memset(recvbuf, 0, 1024);
        //close(sockfd);
        nbyte = read(sockfd, recvbuf, 2);
        //nbyte = recv(sockfd, recvbuf, sizeof(recvbuf),0);
        LOGINFO << ": ret=" << nbyte << ",errno=" << errno << endl;
        //if (-1 == nbyte && errno != EAGAIN) {
        if (-1 == nbyte && errno != EAGAIN) {
            LOGINFO << " read error. errno=" << errno << endl;
            exit(-1);
        }
        if (0 == nbyte) {
            close(sockfd);
            exit(0);
        }
        //LOGINFO << ": read byte="<< nbyte << ",errno=" << errno << ",result="
        //        << recvbuf << endl << endl;
        if (nbyte != -1) {
            //exit(0);
            rn++; 
        }
        LOGINFO << ": shutdown rd." << endl;
        //shRet = shutdown(sockfd, SHUT_RD);
        shRet = close(sockfd);
        if (0 != shRet) {
            LOGINFO << ": shutdown rd error. errno=" << errno <<endl;
        }
        /*
        memset(recvbuf, 0, 1024);
        nbyte = read(sockfd, recvbuf, sizeof(recvbuf));
        //LOGINFO << ": ret=" << nbyte << ",errno=" << errno << endl;
        if (-1 == nbyte && errno != EAGAIN) {
            LOGINFO << " read error. errno=" << errno << endl;
            exit(-1);
        }

        LOGINFO << ": read byte="<< nbyte << ",errno=" << errno << ",result="
                << recvbuf << endl << endl;
        */
    }

    return 0;
}
