-- Transaction practice #1
DROP TABLE users;

-- 자동 COMMIT 비활성화
SET autocommit = 0;

-- users 테이블 생성
CREATE TABLE users (
	id INT AUTO_INCREMENT, 
    name VARCHAR(10) NOT NULL, 
    PRIMARY KEY(id)
);

START TRANSACTION;
INSERT INTO users (name)
VALUES ('harry'), ('test');

SELECT * FROM users;

-- ROLLBACK;
COMMIT;


-- Triggers practice # 1
DROP TABLE articles;
-- 사전 준비 / articles 테이블 작성 및 예시 데이터 입력
CREATE TABLE articles (
	id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL, 
    createdAt DATETIME NOT NULL, 
    updatedAt DATETIME NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO articles (title, createdAt, updatedAt)
VALUES ('title1', CURRENT_TIME(), CURRENT_TIME());

SELECT * FROM articles;

DELIMITER //
CREATE TRIGGER myTrigger
	-- 언제?
    BEFORE UPDATE 
	ON articles FOR EACH ROW
BEGIN
    SET NEW.updatedAt = CURRENT_TIME();
END//
DELIMITER ;

SHOW TRIGGERS;

UPDATE articles
SET title = 'new title'
WHERE id = 1;

-- Triggers practice # 2
-- 트리거를 사용해 기존 게이글이 작성되면, 별도의 테이블에 해당 게시글이 작성되었다는 것을 기록하기
-- 사전 준비
CREATE TABLE articleLogs (
	id INT AUTO_INCREMENT, 
    description VARCHAR(100) NOT NULL, 
    createdAt DATETIME NOT NULL, 
    PRIMARY KEY (id)
);

DELIMITER //
CREATE TRIGGER recordLogs
	AFTER INSERT
    ON articles FOR EACH ROW
BEGIN
	INSERT INTO articleLogs (description, createdAt)
    VALUES ('글이 작성 되었습니다.', CURRENT_TIME());
END//
DELIMITER ;

-- 풀이 확인
INSERT INTO articles (title, createdAt, updatedAt)
VALUES ('title1', CURRENT_TIME(), CURRENT_TIME());

SELECT * FROM articleLogs;

-- Triggers practice #2 심화
-- 트리거를 사용해 기존 게시글이 작성되면, 별도의 테이블에 몇 번 게시글이 작성되었다는 것을 기록하기
DELIMITER //
CREATE TRIGGER recordLogs1
	AFTER INSERT
    ON articles FOR EACH ROW
BEGIN
	INSERT INTO articleLogs (description, createdAt)
    VALUES (CONCAT(NEW.id, '번 글이 작성되었습니다.'), CURRENT_TIME());
END//
DELIMITER ;

SHOW TRIGGERS;

-- Triggers practice #3
-- 트리거를 사용해 기존 게시글이 삭제되면, 삭제된 게시글의 구조 그대로 별도의 테이블에 기록하기
-- 사전 준비
CREATE TABLE backupArticles (
	id INT AUTO_INCREMENT, 
    title VARCHAR(100) NOT NULL, 
    createdAt DATETIME NOT NULL, 
    updatedAt DATETIME NOT NULL, 
    PRIMARY KEY (id)
);

DELIMITER //
CREATE TRIGGER backUpLogs
	AFTER DELETE
    ON articles FOR EACH ROW
BEGIN
	INSERT INTO backupArticles (title, createdAt, updatedAt)
    VALUES (OLD.title, OLD.createdAt, OLD.updatedAt);
END//
DELIMITER ;

-- 풀이 확인
DELETE FROM articles
WHERE id = 3;

SELECT * FROM backupArticles;

SELECT * FROM articles;
SHOW TRIGGERS;
DROP TRIGGER backUpLogs;

--
SELECT * FROM information_schema.INNODB_TRX;
KILL [trx_mysql_thread_id1];