-- 06. midifying Data
CREATE TABLE articles (
  id INT AUTO_INCREMENT,
  title VARCHAR(100) NOT NULL,
  content VARCHAR(200) NOT NULL,
  createdAt DATE NOT NULL,
  PRIMARY KEY (id)
);

SHOW COLUMNS FROM articles;

INSERT INTO articles (title, content, createdAt)
VALUES ('hello', 'world', '2000-01-01');

SELECT * FROM articles;

INSERT INTO
  articles (title, content, createdAt)
VALUES
  ('title1', 'content1', '1900-01-01'),
  ('title2', 'content2', '1800-01-01'),
  ('title3', 'content3', '1700-01-01');

INSERT INTO
  articles (title, content, createdAt)
VALUES
  ('mytitle', 'mycontent', CURDATE());

UPDATE articles
SET title = 'newTitle'
WHERE
  id = 1;

UPDATE
  articles
SET 
  title = 'newTitle2',
  content = 'newContent2'
WHERE id = 2;

UPDATE 
  articles 
SET
  content = REPLACE(content, 'content', 'TEST');

-- set sql_safe_updates=0;

DELETE FROM
  articles
WHERE
  id = 1;

SELECT * FROM articles
ORDER BY createdAt DESC;

DELETE FROM
  articles
ORDER BY
  createdAt DESC
LIMIT 2;