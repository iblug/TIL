-- 문제 1
CREATE TABLE posts (
  postId INT NOT NULL AUTO_INCREMENT,
  title VARCHAR(50) NOT NULL, 
  content VARCHAR(200) NOT NULL,
  PRIMARY KEY (postId)
);

-- 문제 2
ALTER TABLE
  posts
ADD (
  writer VARCHAR(100) DEFAULT 'Anonymous',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 문제 3
ALTER TABLE
  posts
MODIFY
  content text;

-- 문제 4
ALTER TABLE
  posts
DROP COLUMN
  writer;

-- 문제 5
DROP TABLE posts;

-- 문제 6
CREATE TABLE if NOT EXISTS posts (
  postId INT NOT NULL AUTO_INCREMENT, 
  title VARCHAR(50) NOT NULL,
  content TEXT NOT NULL,
  writer varchar(20) NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (postId)
);

-- 문제 7
DROP TABLE if EXISTS posts;

-- test
SELECT * FROM posts;
SHOW COLUMNS FROM posts;