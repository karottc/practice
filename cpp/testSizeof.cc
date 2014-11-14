#include <iostream>
#include <iomanip>

using namespace std;

int main(int argc, char *argv[])
{
    cout.setf(ios::left);
    cout << setw(12) << "char=" << sizeof(char) << "\n";
    cout << setw(12) << "bool=" << sizeof(bool) << "\n";
    cout << setw(12) << "short=" << sizeof(short) << endl;
    cout << setw(12) << "int=" << sizeof(int) << endl;
    cout << setw(12) << "long=" << sizeof(long) << endl;
    cout << setw(12) << "float=" << sizeof(float) << endl;
    cout << setw(12) << "double=" << sizeof(double) << endl;
    cout << setw(12) << "long long=" << sizeof(long long) << endl;
    cout << setw(12) << "long double=" << sizeof(long double) << endl;
    cout << setw(12) << "int*=" << sizeof(int *) << endl;
    cout << setw(12) << "char*=" << sizeof(char *) << endl;
    /* 
     * Linux 2.6.32-220.el6.x86_64 #1 SMP Wed Nov 9 08:03:13 EST 2011 x86_64 x86_64 x86_64 GNU/Linux
     *
     * char=       1
     * bool=       1
     * short=      2
     * int=        4
     * long=       8
     * float=      4
     * double=     8
     * long long=  8
     * long double=16
     * int*=       8
     * char*=      8
     */
    return 0;
}
