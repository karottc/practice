#include <iostream>
#include <unistd.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <string.h>

using namespace std;

int main(int argc, char **argv)
{
    int listenfd, portnumber;
    string input;

    if (argc == 2)
    {
        if ( (portnumber = atoi(argv[1])) < 0)
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

    struct sockaddr_in serveraddr,clientaddr;

    listenfd = socket(AF_INET, SOCK_STREAM, 0);
    memset(&clientaddr, 0, sizeof(clientaddr));
    clientaddr.sin_family = AF_INET;
    string server_addr = "127.0.0.1";
    inet_aton(server_addr.c_str(), &(clientaddr.sin_addr));
    clientaddr.sin_port = htons(9998);
    
    if (bind(listenfd, (sockaddr *)&clientaddr, sizeof(clientaddr)) )
    {
        cerr << "bind failed !!" << endl;
        return 1;
    }
    
    //socklen_t serlen;
    memset(&serveraddr, 0, sizeof(serveraddr));
    serveraddr.sin_family = AF_INET;
    inet_aton(server_addr.c_str(), &(serveraddr.sin_addr));
    serveraddr.sin_port = htons(portnumber);
    if (connect(listenfd,(sockaddr *)&serveraddr, sizeof(serveraddr)))
    {
        cout << "connect failed!!" << endl;
        return 1;
    }
    int n = 0;
    while (1)
    {
        cout << "Please enter: ";
        cin >> input;
        cout << endl;
        n = write(listenfd, input.c_str(), strlen(input.c_str()));
        //n = write(listenfd, input.c_str(), 21);
        cout << "n = " << n << endl;
    }
}
