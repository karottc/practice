select prod_name from products;

SELECT prod_id, prod_name, prod_price FROM Products;

-- DISTINCT: 去重，对后面的所有列都有效
SELECT DISTINCT vend_id FROM Products;

SELECT DISTINCT vend_id, prod_price FROM Products;

-- LIMIT： 取结果的前几位
SELECT prod_name FROM Products LIMIT 5;
-- OFFSET：从第几个开始选择，跟C语言中的偏移量是一样的概念（都是从0开始）
SELECT prod_name FROM Products LIMIT 5 OFFSET 5;