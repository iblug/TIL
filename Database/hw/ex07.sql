-- 데이터 준비
DROP TABLE IF EXISTS `users`;
DROP TABLE IF EXISTS `articles`;

CREATE TABLE IF NOT EXISTS `users` (
	id INT AUTO_INCREMENT, 
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS articles (
	id INT AUTO_INCREMENT, 
    title VARCHAR(50) NOT NULL, 
    content VARCHAR(100) NOT NULL,
    userId INT NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO
	users (name)
VALUES
	('권미자'),
    ('류준하'),
    ('정영식');

INSERT INTO
	articles (title, content, userId)
VALUES
	('제목1', '내용1', 1),
    ('제목2', '내용2', 2),
    ('제목3', '내용3', 4);

-- test
SHOW COLUMNS FROM users;
SELECT * FROM users;
SHOW COLUMNS FROM articles;
SELECT * FROM articles;

-- ex
SELECT articles.id, title, content, name
FROM articles
INNER JOIN users
	ON articles.userId = users.id;

-- INNER JOIN practice #1
SELECT 
    productCode, productName, textDescription
FROM
    products
        INNER JOIN
    productlines ON products.productLine = productlines.productLine;
    
-- INNER JOIN practice #2
SELECT 
    orders.orderNumber,
    status,
    priceEach
FROM
    orders
        INNER JOIN
    orderdetails ON orders.orderNumber = orderdetails.orderNumber;

-- INNER JOIN practice #3
SELECT 
	t1.orderNumber, 
	status,
    SUM(quantityOrdered * priceEach) AS totalSales
FROM
	orders AS t1
		INNER JOIN
	orderdetails AS t2 ON t1.orderNumber = t2.orderNumber
GROUP BY
	t1.orderNumber;

-- LEFT JOIN practice #1
SELECT 
    t1.contactFirstName, orderNumber, status
FROM
    customers AS t1
        LEFT JOIN
    orders AS t2 ON t1.customerNumber = t2.customerNumber;

-- LEFT JOIN practice #2
SELECT 
    t1.contactFirstName, orderNumber, status
FROM
    customers AS t1
        LEFT JOIN
    orders AS t2 ON t1.customerNumber = t2.customerNumber
WHERE
    orderNumber IS NULL;

-- RIGHT JOIN practice #1
SELECT 
    employeeNumber, firstName, customerNumber, contactFirstName
FROM
    customers
        RIGHT JOIN
    employees ON customers.salesRepEmployeeNumber = employees.employeeNumber;
    
-- RIGHT JOIN practice #2
SELECT 
    employeeNumber, firstName, customerNumber, contactFirstName
FROM
    customers
        RIGHT JOIN
    employees ON customers.salesRepEmployeeNumber = employees.employeeNumber
WHERE
	customerNumber IS NULL;

