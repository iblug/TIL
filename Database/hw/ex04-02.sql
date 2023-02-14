-- DISTINCT practice #2
SELECT DISTINCT
    lastName
FROM
    employees
ORDER BY lastName ASC;

-- WHERE practice #1
SELECT 
    lastName, firstName, officeCode
FROM
    employees
WHERE
    officeCode = 1;

-- WHERE practice #2
SELECT
	lastName, firstName, jobTitle
FROM
	employees
WHERE
	jobTitle != 'Sales Rep';
    
-- WHERE practice #3
SELECT 
    lastName, firstName, officeCode, jobTitle
FROM
    employees
WHERE
    officeCode >= 3
        AND jobTitle = 'Sales Rep';

-- WHERE practice #4
SELECT 
    lastName, firstName, officeCode, jobTitle
FROM
    employees
WHERE
    officeCode < 5
        OR jobTitle != 'Sales Rep';
        
-- WHERE practice #5
SELECT 
    lastName, firstName, officeCode
FROM
    employees
WHERE
--     officeCode >= 1 AND officeCode <= 4;
	officeCode BETWEEN 1 AND 4;

-- WHERE practice #6
SELECT 
    lastName, firstName, officeCode
FROM
    employees
WHERE
    officeCode BETWEEN 1 AND 4
ORDER BY officeCode;

-- WHERE practice #7
SELECT 
    lastName, firstName, officeCode
FROM
    employees
WHERE
    officeCode IN (1 , 3, 4);
    
-- WHERE practice #8
SELECT 
    lastName, firstName, officeCode
FROM
    employees
WHERE
    officeCode NOT IN (1 , 3, 4);
    
-- WHERE practice #9
SELECT 
    lastName, firstName
FROM
    employees
WHERE
    lastName LIKE '%son'; -- wildcard

-- WHERE practice #10
SELECT 
    lastName, firstName
FROM
    employees
WHERE
    firstName LIKE '___y';
    
-- LIMIT practice #1
SELECT 
    firstName, officeCode
FROM
    employees
ORDER BY officeCode DESC
LIMIT 7;

-- LIMIT practice #2
SELECT 
    firstName, officeCode
FROM
    employees
ORDER BY officeCode DESC
LIMIT 3 , 5;

-- GROUP BY 1/2
SELECT 
    jobTitle
FROM
    employees
GROUP BY jobTitle;

-- GROUP BY 2/2
SELECT
	jobTitle, COUNT(*)
FROM
	employees
GROUP BY
	jobTitle;

-- GROUP BY practice #1
SELECT
	country, AVG(creditLimit) AS avgOfCreditLimit
FROM
	customers
GROUP BY
	country
ORDER BY
	avgOfCreditLimit DESC;
    
-- GROUP BY practice #2
SELECT
	country, AVG(creditLimit)
FROM
	customers
GROUP BY
	country
HAVING
 	AVG(creditLimit) > 80000;

-- NULL
SELECT
	postalCode
FROM
	customers
ORDER BY
	postalCode;

-- NULL 처리
SELECT
	postalCode
FROM
	customers
WHERE
	postalCode is not NULL
ORDER BY
	postalCode;