## 《Beginning Python(2rd)》 ##

这本书的中文名是 *《Python基础教程(第二版)》* ，下面列出来的代码都是源于我在看这本书的书的时候产生的代码，有些是书中例子，有些是自己的一些想法的实验，然后可能会有一些结论：

1. index_20140619.py：这是第二章的的一个索引的例子。从这个例子知道，Python对中文的支持还不够，如果`.py`的文件中有中文(**在注释中的中文也算**)就需要找文件开始声明 `# coding=UTF-8 `，并且 `coding` 和 `=` 之间不能有空格( *好像 `# encoding=UTF-8`* 也可以，我测试通过)。
2. multi_20140619.py：乘法示例。在盒子中输出字符串，此例书中代码有错.
3. permisson_20140620.py：测试成员资格示例，即 `in` 表达式的用法，是否为子串。
4. list_20140620.py：测试列表操作，`list` 函数等，extend、index方法。
5. str_20140622.py：格式化字符串。
6. str_method_20140622.py：字符串的一些函数，`strip`方法识别最后一个函数是通过最后一个单词的空格来识别的，比如本例子中的`!`和`*`之间如果有空格就只能去掉`*`符号。
7. dict_20140622.py：字典操作。
8. dict_method_20140622.py：字典的一些方法示例。
9. print_20140523.py：`print`和赋值。
10. if_20140623.py：if语句。
11. while_20140623.py：while循环、for循环。zip可以用于不等长的序列。
12. multitable_20140624.py：输出一个 **9x9的乘法表**，综合使用for循环和print语句，以及元组。
13. function_20140625.py：一些函数示例。
14. more_function_20140627.py：练习使用函数的参数。
15. global_params_20140627.py：全局变量和局部变量。
16. recur_20140628.py：递归函数示例。
17. class_20140630.py：class的示例，建议在有class的文件开始的处添加一行 `__metaclass__=type` ,这样表示使用新式类。
18. exception_20140701.py：异常捕捉示例。
19. class_more_20140702.py：魔法方法、属性和迭代器示例。python的构造函数是 `def __init__(self):` ,析构函数是 `__del__(self)` ，析构函数的调用时间点不确定，一般是程序结束的时候，在子类中初始化父类用 `super` 函数，用法为： `super(childclassname, self).__init__()` ；使用`@`操作符来表示静态方法；生成器的使用，这个好像是python里面新的东西我在C/C++以及java/C#里面都没碰到过。
20. generator_20140705.py：生成器的方法，**注：** 使用send方法(而不是next方法)只有在生成器挂起之后才有意义(也就是说在yield函数第一次执行之后)。
21. eight_empress_20140705.py：八皇后问题的python解法，非常简洁，当皇后数量n较大的时候，运行速度就比较慢了。
22. eight_empress.c：八皇后问题非常高效的C语言实现方法,但是用的也是回溯法。
23. import_20140710.py：同时包括了 hello_20140710.py 文件，这个是使用 `import` 来导入自己的模块的示例。
24. reverseargs.py：反序输出变量，系统函数示例。
25. shelve_20140712.py：系统库 `shelve` 的文件操作示例。
26. file_20140714.py：文件操作的一些示例。
27. sqlite_20140717.py：使用SQLite的示例，基本的对数据库表的创建和插入操作；ABBREV.txt，这是输入数据库的源文件。
28. food_query_20140715.py：这个是对上面生成数据库的查询操作。
29. socket_server_20140718.py, socket_client_20140718.py：简单的socket的服务端和客户端的示例。
30. select_20140718.py, pull_20140718.py：使用select和pull两种异步IO方式来实现的简单服务器。
31. htmlParser_20140720.py：使用tidy的urllib的示例。
32. urllib_20140730.py：第15章，网页抓取内容的示例，