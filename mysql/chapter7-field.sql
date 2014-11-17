-- 拼接字段+或者||或者使用函数，MYSQL和MariaDB中需要使用函数
SELECT vend_name + '(' + vend_country + ')' FROM Vendors ORDER BY vend_name;
-- MYSQL的语句
SELECT Concat(vend_name,'(',vend_country,')') FROM Vendors ORDER BY vend_name;

-- AS 别名，作为一个计算字段的替换名
SELECT Concat(vend_name,'(',vend_country,')') AS vend_title FROM Vendors ORDER BY vend_name;

-- 算术运算,算术操作可以用括号来区分运算顺序
SELECT prod_id, quantity, item_price, quantity*item_price AS expanded_price FROM OrderItems WHERE order_num = 20008;
