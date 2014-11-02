/* 测试STL的priority_queue */

#include <iostream>
#include <vector>
#include <queue>
#include <functional>
#include <string>

using namespace std;

// Empty the priority queue and print its contents.
template <typename PriorityQueue>
void dumpContents(const string &msg, PriorityQueue &pg)
{
    cout << msg << ":" << endl;
    while (!pg.empty())
    {
        cout << pg.top() << endl;
        pg.pop();
    }
}

// Do some inserts and removes (done in dumpContents).
int main()
{
    priority_queue<int> maxPQ;    // 默认就是最大值堆
    priority_queue<int,vector<int>,greater<int> > minPQ;

    minPQ.push(4);
    minPQ.push(3);
    minPQ.push(5);
    
    maxPQ.push(4);
    maxPQ.push(3);
    maxPQ.push(5);

    dumpContents("minPQ", minPQ);
    dumpContents("maxPQ", maxPQ);
}
