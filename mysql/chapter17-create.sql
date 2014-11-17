-- CREATE TABLE时必须给出下面信息：
-- 1.新表的名字，在关键字CREATE TABLE之后给出；
-- 2.表列的名字和定义，用逗号分隔；
-- 3.有的DBMS还要求指定表的位置。
-- 不指定属性，默认是NULL值
CREATE TABLE Products_test
(
	cust_id  	CHAR(10)  		NOT NULL,
    vend_id 	CHAR(10) 		NOT NULL,
    prod_name 	CHAR(254) 		NOT NULL,
    prod_price  DECIMAL(8,2) 	NOT NULL,
    prod_desc 	text 			NULL
);

CREATE TABLE Orders_test
(
	order_num 	int 		NOT NULL,
    order_date  datetime 	NOT NULL,
    cust_id 	CHAR(10) 	NOT NULL
);

-- 更新表
-- 使用ALTER table
ALTER TABLE Vendors ADD vend_phone CHAR(20);
-- 删除列
ALTER TABLE Vendors DROP COLUMN vend_phone;

-- 删除表
DROP TABLE Products_test;

-- 重命名表：RENAME