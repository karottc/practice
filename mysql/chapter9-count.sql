-- 汇总数据
-- AVG() 函数，计算平均值,AVG会忽略值为NULL的行
SELECT AVG(prod_price) AS avg_price FROM Products;
SELECT AVG(prod_price) AS avg_price FROM Products WHERE vend_id = 'DLL01';

-- COUNT，统计，COUNT(*)对所有行进行统计，COUNT(column)对具有值行进行统计
SELECT COUNT(*) AS num_cust FROM Customers;
SELECT COUNT(cust_email) AS num_cust FROM Customers;

-- MAX() 返回指定列中的最大值,也可用于文本，用于文本是返回排序后的最后一行
SELECT MAX(prod_price) AS max_price FROM Products;

-- MIN() 返回指定列中的最小值，和MAX一样，也可以用于文本
SELECT MIN(prod_price) AS MIN_price FROM Products;

-- SUM() 返回指定列值的总计,SUM也会忽略值为NULL的行
SELECT SUM(quantity) AS item_ordered FROM OrderItems WHERE order_num = 20005;
SELECT SUM(quantity*item_price) AS total_price FROM OrderItems WHERE order_num = 20005;

-- 只求不同值的平均价格
SELECT AVG(DISTINCT prod_price) AS avg_price FROM Products WHERE vend_id = 'DLL01';

-- 组合聚集函数
SELECT COUNT(*) AS num_item, MIN(prod_price) AS price_min, MAX(prod_price) AS price_max, AVG(prod_price) AS price_avg FROM Products;