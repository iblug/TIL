-- 문제 1
SELECT productCode, productName, MSRP
FROM products
WHERE MSRP > (
	SELECT AVG(MSRP)
    FROM products
)
ORDER BY
	MSRP ASC;

-- 문제 2
SELECT customerNumber, customerName
FROM customers
WHERE customerNumber IN (
	SELECT customerNumber
	FROM orders
	WHERE orderDate BETWEEN '2003-01-06' AND '2003-03-26'
)
ORDER BY
	customerNumber;
    
-- 문제 3
SELECT productCode, productName, productLine, MSRP
FROM products
WHERE MSRP = (
	SELECT MAX(MSRP)
	FROM products
	WHERE
		productLine = 'Classic Cars'
);

-- 문제 4
SELECT customerNumber, customerName, country
FROM customers
WHERE country = (
	SELECT country
	FROM customers
	GROUP BY
		country
	ORDER BY
		COUNT(country) DESC
	LIMIT 1
)
ORDER BY
	1;

-- 정렬 없이
SELECT customerNumber, customerName, country
FROM customers
WHERE country = (
	SELECT MAX(country)
    FROM customers
)
ORDER BY 1;

-- 문제 5
-- 가장 많은 주문(order)을 한 고객(customer)의 
-- customerNumber , customerName , 주문 수(order_count) 를 조회하시오.
-- 고객 데이터는 customers 테이블, 주문 테이블은 orders 테이블을 활용합니다.
SELECT L.customerNumber, customerName, order_count
FROM customers L
INNER JOIN (
	SELECT customerNumber, COUNT(customerNumber) as order_count
	FROM orders
	GROUP BY
		customerNumber
	ORDER BY
		2 DESC
	LIMIT 1
) as R
	ON L.customerNumber = R.customerNumber;

-- 다른 답
SELECT 
	t1.customerNumber, 
    customerName,
    COUNT(*) AS order_count 
FROM orders t1
INNER JOIN customers t2
	ON t1.customerNumber = t2.customerNumber
GROUP BY t1.customerNumber
ORDER BY order_count DESC
LIMIT 1;

-- 다른 답
SELECT c.customerNumber, c.customerName, COUNT(*) as order_count
FROM customers c
INNER JOIN orders o 
	ON c.customerNumber = o.customerNumber
WHERE c.customerNumber = (
    SELECT customerNumber
    FROM orders
    GROUP BY customerNumber
    ORDER BY COUNT(customerNumber) DESC
    LIMIT 1
)
GROUP BY c.customerNumber, c.customerName;

-- (order 없이)
SELECT c.customerNumber, c.customerName, COUNT(o.orderNumber) AS order_count
FROM customers c
JOIN orders o ON c.customerNumber = o.customerNumber
GROUP BY c.customerNumber, c.customerName
HAVING COUNT(o.orderNumber) = (
  SELECT MAX(order_count)
  FROM (
    SELECT COUNT(orderNumber) AS order_count
    FROM orders
    GROUP BY customerNumber
  ) t
);


-- 문제 6
SELECT DISTINCT t1.productCode, productName
FROM orderdetails t1
INNER JOIN products t2
	ON t1.productCode = t2.productCode
WHERE orderNumber IN (
	SELECT orderNumber
	FROM orders
	WHERE YEAR(orderDate) = 2004
)
ORDER BY
	productCode DESC;

-- 다른 답 (join 두번)
SELECT DISTINCT p.productCode, p.productName
FROM orders o
INNER JOIN orderdetails od ON o.orderNumber = od.orderNumber
INNER JOIN products p ON od.productCode = p.productCode
WHERE YEAR(o.orderDate) = 2004
ORDER BY p.productCode DESC;



SHOW COLUMNS FROM products;
SHOW COLUMNS FROM customers;
SELECT * FROM customers;
SHOW COLUMNS FROM orders;
SELECT * FROM orders;
SHOW TABLES;

SELECT * FROM customers;

