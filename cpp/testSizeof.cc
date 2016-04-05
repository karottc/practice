#include <iostream>
#include <iomanip>
#include <limits>

using namespace std;

typedef int Py_ssize_t;

#define Objecet_EXTRA_HEAD \
    char *next; \
    char *prev;

#define Objecet_HEAD \
    Objecet_EXTRA_HEAD \
    Py_ssize_t refcnt; \
    char *ob_type;

typedef struct {
    Objecet_HEAD
    long ob_ival;
}Py_test_size;

int main(int argc, char *argv[])
{
    cout.setf(ios::left);
    cout << setw(12) << "char=" << sizeof(char) << " byte, longest=" << numeric_limits<char>::max() << "\n";
    cout << setw(12) << "bool=" << sizeof(bool) << " byte, longest=" << numeric_limits<bool>::max() << "\n";
    cout << setw(12) << "short=" << sizeof(short) << " byte, longest=" << numeric_limits<short>::max() << endl;
    cout << setw(12) << "int=" << sizeof(int) << " byte, longest=" << numeric_limits<int>::max() << endl;
    cout << setw(12) << "long=" << sizeof(long) << " byte, longest=" << numeric_limits<long>::max() << endl;
    cout << setw(12) << "float=" << sizeof(float) << " byte, longest=" << numeric_limits<float>::max() << endl;
    cout << setw(12) << "double=" << sizeof(double) << " byte, longest=" << numeric_limits<double>::max() << endl;
    cout << setw(12) << "long long=" << sizeof(long long) << " byte, longest=" << numeric_limits<long long>::max() << endl;
    cout << setw(12) << "long double=" << sizeof(long double) << " byte, longest=" << numeric_limits<long double>::max() << endl;
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
    cout << "--------------------------------------------------------------------------" << endl;
    cout << setw(12) << "sturctSize=" << sizeof(Py_test_size) << endl;
    return 0;
}
