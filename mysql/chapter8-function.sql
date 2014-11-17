-- 使用函数处理数据
-- 不同的DBMS，函数的差异较大，在程序中应给出充分的注释，方面以后移植
SELECT vend_name, UPPER(vend_name) AS vend_name_upcase FROM Vendors ORDER BY vend_name;
-- SOUNDEX 将字符串根据语音表示来搜索， MS Access和PostgreSQL不支持这个函数
SELECT cust_name, cust_contact FROM Customers WHERE SOUNDEX(cust_contact) = SOUNDEX('Michael Green');

-- 日期函数在DBMS之中可移植性最差
-- SELECT order_num FROM Orders WHERE DATEPART(yy, order_date) = 2012;
SELECT order_num FROM Orders WHERE YEAR(order_date) = 2012;  -- MYSQL写法

-- 一些数值处理函数，DBMS之中，大多相同
-- ABS(),COS(),EXP(),PI(),SIN(),SQRT(),TAN()