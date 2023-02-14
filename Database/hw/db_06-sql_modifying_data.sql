-- 문제 1
CREATE TABLE users (
    userId INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    birthday DATE NOT NULL,
    city VARCHAR(100),
    country VARCHAR(100),
    email VARCHAR(100),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (userId)
);

-- 문제 2
INSERT INTO users (first_name, last_name, birthday, city, country, email)
VALUES 
	('Beemo', 'Jeong', '1000-01-01', '', '', 'beemo@hphk,kr'),
    ('Jieun', 'Lee', '1993-05-16', 'Seoul', 'Korea', ''),
    ('Dami', 'Kim', '1995-04-09', 'Seoul', 'Korea', ''),
    ('Kwangsoo', 'Lee', '1985-07-14', 'Seoul', 'Korea', '');

-- 문제 3
INSERT INTO users (first_name, last_name, birthday, city, country, email)
VALUES
  ("Ann Day","Carter","1997-03-10","AL","France","carter@yahoo.couk"),
  ("Declan Wang","Calvin","1991-07-12","AR","United Kingdom","calvin4061@yahoo.net"),
  ("Hillary Tran","Walter","2000-08-10","Jeonnam","South Korea","walter8920@icloud.ca"),
  ("Fatima Anderson","Desiree","1999-12-23","NI","Germany","desiree@yahoo.couk"),
  ("Yen Patel","Erin","1993-04-02","Gangwon","South Korea","erin6940@icloud.net");

-- 문제 4
UPDATE
	users
SET
	first_name = 'Gwangbae',
    last_name = 'Jeong',
    birthday = '1993-11-15'
ORDER BY
	userId ASC
LIMIT 4;

-- 문제 5
UPDATE
	users
SET
	country = 'Korea'
WHERE
	country = '';

-- 문제 6
DELETE FROM users
WHERE
	first_name = 'Beemo';

-- 문제 7
DELETE
FROM users
WHERE
	first_name = 'Kwangsoo' AND
    last_name = 'Lee';

-- 문제 8
DELETE
FROM users
ORDER BY
	created_at DESC
LIMIT 1;

-- test
SHOW COLUMNS FROM users;
SELECT * FROM users;

set sql_safe_updates=0;

-- drop
DROP TABLE users;