#include <arpa/inet.h>
#include <iostream>

using namespace std;

int main(void)
{
    // 判断主机字节序
    union Endian
    {
        int num;
        char ch[4];
    };
    union Endian tEndian;
    tEndian.num = 0x12345678;
    cout << "This mechiane's byte order: ";
    if (0x12 == tEndian.ch[0]) {
        cout << "Big Endian" << endl;
    } else if (0x78 == tEndian.ch[0]) { 
        cout << "Little Endian" << endl;
    } else {
        cout << "byte order error." << endl;
    }
    // byte order end.
    cout << "***************************************" << endl;
    // 判断网络字节序是否和主机字节序相同
    // 网络字节序是大端字节序
    uint32_t dwHost = 0x12345678;
    uint32_t dwNet = htonl(dwHost);
    cout << "host byte:0x" << hex << dwHost << ",network byte:0x" << hex << dwNet << endl;
    
    cout << "***************************************" << endl;
    cout << "int = " << sizeof(int) << " byte\n" << "short = " << sizeof(short)
         << " byte\n" << "long = " << sizeof(long) << " byte\n" << "long long = "
         << sizeof(long long) << " byte\n" << "char * = " << sizeof(char *) << endl;
    // 64 bit 机器：int = 4, short = 2, long = 8, long long = 8, char * = 8, 
    // 32 bit 机器：int = 4, short = 2, long = 4, long long = 8, char * = 4, 
    cout << "***************************************" << endl;
    return 0;
}
