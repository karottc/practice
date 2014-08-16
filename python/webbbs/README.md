## 电子公告板 ##

本project是实现一个电子公告板，类似于一个论坛的跟帖机制。

最终的系统应该支持下面的功能：

* 显示所有当前消息的主题
* 支持消息的线程处理(显示针对回复消息的所有回复消息)
* 查看已经存在的消息
* 回复已经存在的消息

在以上基础上的更高要求的功能：

* 可以非常稳定处理大量消息
* 避免诸如两个用户同时写入一个文件之类的问题


----------------

database.py：sqlite3的数据库文件；

simple_main.py：第一次的简单实现，可以基本运行，但是结果有点不对。