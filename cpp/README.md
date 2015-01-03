## About ##

一些测试和练习代码：

1. [timerExample.c](timerExample.c)： POSIX下的timer例子，在linux下是OK的，在mac os下暂不能使用，因为Mac OS没有实现POSIX的timer;
2. [forkReadFile.c](forkReadFile.c): 测试多个进程对同一个文件的读、写、append的情况对文件的影响;
3. [test_priority_queue.cc](test_priority_queue.cc): 测试对priority_queue的使用,priority_queue<int> 默认是一个最大堆;
4. [testSizeof.cc](testSizeof.cc): 测试当前平台下的基本类型占用字节数，sizeof(int)等等;
5. [vector-test.cpp](vector-test.cpp): 对STL中的vector的特性测试;
6. [map-test.cpp](map-test.cpp): 对STL中map的特性测试,下标操作[]会引起心新插入一个节点，map自带的find操作比STL的公用的find操作更有效率，因为STL的find操作只是循环搜寻；
7. [set-test.cpp](set-test.cpp): 对STL中的set的特性测试，set的元素的值只有0和1两种,不同通过迭代器来改变元素，比如`*iter = 9`是错误的。
