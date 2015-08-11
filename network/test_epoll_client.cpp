#include <sys/socket.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>
#include <stdlib.h>

#include <iostream>
#include <string>

using namespace std;

#define LOGINFO cout << __FUNCTION__ << ":" << __LINE__
#define PORT 8090



int main(void)
{
    int sockfd;
    int rc;
    int cpid;
    struct sockaddr_in servaddr;

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

    while (1) {
        cout << endl;
        LOGINFO << ": fd=" << sockfd << endl;
        char input[1024];
        cout << "Please input: ";
        cin >> input;
        int nbyte = write(sockfd, input, strlen(input));
        if (-1 == nbyte) {
            LOGINFO << " write error. " << endl;
            exit(-1);
        }

        char recvbuf[1024];
        nbyte = read(sockfd, recvbuf, sizeof(recvbuf));
        if (-1 == nbyte) {
            LOGINFO << " write error. " << endl;
            exit(-1);
        }

        LOGINFO << ": result=" << recvbuf << endl << endl;
    }

    return 0;
}
