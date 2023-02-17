-- Subquery practice #1
-- 가장 많은 돈을 소비한 고객 번호 조회
SELECT customerNumber, amount
FROM payments
WHERE amount = (
    SELECT MAX(amount) FROM payments
);
--
SELECT customerNumber, amount
FROM payments
ORDER BY
	amount DESC
LIMIT 1;

-- Subquery practice #2
-- 미국에 있는 사무실에서 근무하는 직원의 이름과 성 조회
SELECT lastName, firstName
FROM employees
WHERE officeCode IN (
    SELECT officeCode 
    FROM offices 
    WHERE country = 'USA'
);

-- Subquery practice #3
-- 주문한 적이 없는 고객 목록 조회
SELECT customerName
FROM customers
WHERE customerNumber NOT IN (
	SELECT DISTINCT customerNumber
    FROM orders
);
-- JOIN 활용
SELECT customerName
FROM customers
WHERE customerNumber IN (
	SELECT L.customerNumber
	FROM customers L
	LEFT JOIN orders
		ON L.customerNumber = orders.customerNumber
	WHERE
		orderNumber is NULL
);
SELECT * FROM orders;
SELECT * FROM customers;

-- Subquery practice #ad
-- 소비를 한 고객들 중 한번에 지불한 금액이 가작 높은 고객의 customerNumber, amount, contactFirstName 조회
SELECT L.customerNumber, amount, contactFirstName
FROM customers L
LEFT JOIN payments
	ON L.customerNumber = payments.customerNumber
WHERE amount = (
	SELECT MAX(amount)
    FROM payments
);
-- 예시 답
SELECT customerNumber, amount, contactFirstName
FROM (
	SELECT contactFirstName, amount, L.customerNumber
    FROM customers L -- payments
    INNER JOIN payments USING (customerNumber)
) as findName
WHERE amount = (SELECT MAX(amount) FROM payments);

-- EXISTS practice #1
SELECT customerNumber, customerName
FROM customers
WHERE EXISTS (
	SELECT customerNumber
    FROM orders
    WHERE customers.customerNumber = orders.customerNumber
);

-- EXISTS practice #2
SELECT employeeNumber, firstName, lastName
FROM employees
WHERE EXISTS (
	SELECT *
    FROM offices
    WHERE city = 'Paris' AND offices.officeCode = employees.officeCode
);

SELECT lastName, firstName
FROM employees
WHERE officeCode IN (
    SELECT officeCode 
    FROM offices 
    WHERE city = 'Paris'
);

-- CASE practice #1
SELECT contactFirstName, creditLimit,
	CASE
		WHEN creditLimit > 100000 THEN 'VIP'
        WHEN creditLimit > 70000 THEN 'Platinum'
        ELSE 'Bronze'
	END AS grade
FROM customers;

-- CASE practice #2
SELECT orderNumber, status, 
	CASE 
		WHEN status = 'Shipped' THEN '발주완료'
        WHEN status = 'In Process' THEN '주문중'
        WHEN status = 'Cancelled' THEN '주문취소'
        ELSE '기타사유'
	END AS details
FROM orders;

SELECT * FROM employees;
SELECT * FROM offices;
