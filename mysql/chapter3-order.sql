-- ORDER BY 子句应该是 SELECT语句中的最后一个子句，否则将报错
SELECT prod_name FROM Products ORDER BY prod_name;

-- 下面语句中，只有在有多个相同的prod_price时才对prod_name排序，如果prod_price是唯一的，则不会对prod_name进行排序
SELECT prod_id, prod_price, prod_name FROM Products ORDER BY prod_price, prod_name;

-- ORDER BY 也可以使用相对位置来进行排序
SELECT prod_id, prod_price, prod_name FROM Products ORDER BY 2, 3;

-- DESC (DESCENDING)表示降序排列,ASC(ASCENDING)表示升序排列，默认是升序
SELECT prod_id, prod_price, prod_name FROM Products ORDER BY prod_price DESC;
-- 如果在要多个列上执行降序，必须在每一个列上指定 DESC
SELECT prod_id, prod_price, prod_name FROM Products ORDER BY prod_price DESC, prod_name;