/* 第三章：标准库预览
 * Page 55
 * istream_iterator and ostream_iterator
 */
#include <iostream>
// ifstream 变量所用头文件
#include <fstream>
// istream_iterator 类型所用头文件
#include <iterator>
// vector类型的头文件
#include <vector>
// unique_copy / sort 所用头文件
#include <algorithm>

using namespace std;

int main()
{
    string from, to;
    cin >> from >> to;  // 取得源文件和目标文件名

    ifstream is(from.c_str());  // 输入流
    istream_iterator<string> ii(is);    // 流的输入迭代器
    istream_iterator<string> eos;       // 输入的哨兵

    vector<string> b(ii, eos);  // b是一个vector，用输入进行初始化
    sort(b.begin(), b.end());   // 对缓冲区排序

    ofstream os(to.c_str());    // 输出流
    ostream_iterator<string>  oo(os, "\n");   // 流的输出迭代器

    unique_copy(b.begin(), b.end(), oo); // 从缓冲区复制到输出，并去掉重复的值

    return !is.eof() || !os;
}
