-- 用WHERE建立更高级的搜索条件
-- AND 操作符
SELECT prod_id, prod_price, prod_name FROM Products WHERE vend_id = 'DLL01' AND prod_price <= 4;

-- OR 操作符，表示匹配任意条件，第一个条件满足就不会去判断第二个条件了
SELECT prod_name, prod_price FROM Products WHERE vend_id = 'DLL01' OR vend_id = 'BRS01';

-- 默认情况AND的优先级高于OR的优先级，所以需要使用括号
SELECT prod_name, prod_price FROM Products WHERE (vend_id = 'DLL01' OR vend_id = 'BRS01') AND prod_price >= 10;

-- IN 操作符，取值为括号内的值, IN可以代替OR操作符，比OR操作符执行的更快，并且IN可以包含其他SELECT子句
SELECT prod_name, prod_price FROM Products WHERE vend_id IN ('DLL01', 'BRS01') ORDER BY prod_name;

-- NOT 操作符，否定其后跟的所有条件,通常和IN配合使用
SELECT prod_name FROM Products WHERE NOT vend_id = 'DLL01' ORDER BY prod_name;