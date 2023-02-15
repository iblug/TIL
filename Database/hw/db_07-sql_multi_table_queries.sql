-- 문제 1
SELECT 
	employeeNumber, 
    lastName, 
    firstName, 
    city
FROM employees
INNER JOIN offices
	ON employees.officeCode = offices.officeCode
ORDER BY
	employeeNumber;

-- 문제 2
SELECT 
	customerNumber,
    officeCode, 
    customers.city, 
    offices.city
FROM customers
LEFT JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;

-- 문제 3
SELECT
	customerNumber, 
    officeCode,
    customers.city,
    offices.city
FROM customers
RIGHT JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;

-- 문제 4
SELECT
	customerNumber, 
    officeCode, 
    customers.city, 
    offices.city
FROM customers
INNER JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;
    
-- 문제 5
-- 왼쪽 테이블(coustomers), 오른쪽 테이블(offices)
-- LEFT JOIN은 왼쪽은 무조건 표시하고 오른쪽에 매치되는 레코드가 없으면 NULL표시,
-- RIGHT JOIN은 오른쪽은 무조건 표시하고 왼쪽에 매치되는 레코드가 없으면 NULL표시,
-- INNER JOIN은 두 테이블에 매치되는 레코드에 대해서만 결과를 표시

-- 문제 6
SELECT 
	customerNumber, 
    officeCode, 
    customers.city, 
    offices.city
FROM customers
LEFT JOIN offices
	ON customers.city = offices.city
UNION
SELECT
	customerNumber, 
    officeCode, 
    customers.city, 
    offices.city
FROM customers
RIGHT JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;

-- show
SHOW COLUMNS FROM orderdetails;
SHOW COLUMNS FROM orders;
SHOW COLUMNS FROM products;

-- 문제 7
SELECT 
	t1.orderNumber, 
    orderDate
FROM orderdetails AS t1
INNER JOIN orders
	ON t1.orderNumber = orders.orderNumber
ORDER BY
	orderNumber ASC;
    
-- 문제 8
SELECT
	t1.orderNumber, 
    t2.productCode, 
    productName
FROM orderdetails AS t1
INNER JOIN products AS t2
	ON t1.productCode = t2.productCode
ORDER BY
	1;
    
-- 문제 9
-- orderdetails 기준
SELECT
	t1.ordernumber, -- t1, t2에 따라 정렬이 달라짐..
    t1.productCode, 
    t2.orderDate, 
    t3.productName
FROM orderdetails AS t1
INNER JOIN orders AS t2
	ON t1.orderNumber = t2.orderNumber
INNER JOIN products AS t3
	ON t1.productCode = t3.productCode
ORDER BY
	1;
    
-- order 기준
SELECT
	t1.ordernumber, -- t1, t2에 따라 정렬이 달라짐
    t2.productCode, 
    t1.orderDate, 
    t3.productName
FROM orders AS t1
INNER JOIN orderdetails AS t2
	ON t1.orderNumber = t2.orderNumber
INNER JOIN products AS t3
	ON t2.productCode = t3.productCode
ORDER BY
	1;

-- NATURAL JOIN
-- orderdetails 기준
SELECT
    orderNumber,
    productCode,
    orderDate,
    productName
FROM orderdetails
NATURAL JOIN (orders,products)
ORDER BY orderNumber;

-- order 기준
SELECT
    orderNumber,
    productCode,
    orderDate,
    productName
FROM orders
NATURAL JOIN orderdetails
NATURAL JOIN products
ORDER BY orderNumber;