#include <map>
#include <iostream>
#include <string>

using namespace std;

int main()
{
    map<string, int> simap;
    simap[string("jjhou")] = 1;
    simap[string("jerry")] = 2;
    simap[string("jason")] = 3;
    simap[string("jimmy")] = 4;

    pair<string, int> value(string("david"), 5);
    simap.insert(value);

    // 下标操作[] 是插入操作。
    //int nu = simap[string("jjhouxxx")];
    //cout << nu << endl;
    
    map<string, int>::iterator simap_iter = simap.begin();
    for (; simap_iter != simap.end(); ++simap_iter)
    {
        cout << simap_iter->first << ' ' << simap_iter->second << endl;
    }

    int number = simap[string("jjhou")];
    cout << number << endl;


    map<string, int>::iterator itel;

    // 面对关联式容器，应该使用其所提供的find函数来搜寻元素，会比使用STL算法
    // find()更有效率，因为STL算法find()只是循环搜寻
    itel = simap.find(string("mchen"));
    if (itel == simap.end())
        cout << "mchen not found" << endl;

    itel = simap.find(string("jerry"));
    if (itel != simap.end())
        cout << "jerry found" << endl;

    itel->second = 9;
    int number2 = simap[string("jerry")];
    cout << number2 << endl;

    return 0;
}
