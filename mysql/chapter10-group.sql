-- 分组数据
-- 比如要返回每个供应商的产品数目，怎么办
-- 创建分组,使用了GROUP 就会对每个分组而不是整体进行聚集
SELECT vend_id, COUNT(*) AS num_prods FROM Products GROUP BY vend_id;

-- HAVING,分组过滤, HAVING支持所有支持WHERE的操作
SELECT cust_id, COUNT(*) AS orders FROM Orders GROUP BY cust_id HAVING COUNT(*) >= 2;
-- WHERE是在分组前进行过滤，HAVING是在分组后进行过滤;下面语句，先用where把行选出来，然后再根据vend_id分组，最后用HAVING选出分组
SELECT vend_id, COUNT(*) AS num_prods FROM Products WHERE prod_price >= 4 GROUP BY vend_id HAVING COUNT(*) >= 2;

-- 如果需要排序最好明确使用ORDER BY
SELECT order_num, COUNT(*) AS items FROM OrderItems GROUP BY order_num HAVING COUNT(*) >= 3;
SELECT order_num, COUNT(*) AS items FROM OrderItems GROUP BY order_num HAVING items >= 3 ORDER BY items;

-- SELECT 语句中的子句顺序：
-- SELECT->FROM->WHERE->BROUP BY->HAVING->ORDER BY