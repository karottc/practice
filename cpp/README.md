## About ##

一些测试和练习代码：

1. timerExample.c： POSIX下的timer例子，在linux下是OK的，在mac os下暂不能使用，因为Mac OS没有实现POSIX的timer;
2. forkReadFile.c: 测试多个进程对同一个文件的读、写、append的情况对文件的影响;
3. test_priority_queue.cc: 测试对priority_queue的使用,priority_queue<int> 默认是一个最大堆;