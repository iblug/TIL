# SQL - Basics

## 목차
1. Introduction to SQL
2. SQL Statements

## 학습 목표
* 데이터베이스에서 SQL의 역할을 정의할 수 있다.
* SQL 명령의 종류를 동작에 따라 3가지 이상 열거할 수 있다.
* 표준 SQL 문법을 식별할 수 있다.

# 1. Introduction to SQL
* SQL(Structure Query Language): 테이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어
* 관계형 데이터베이스와의 대화
## SQL Syntax
* google: `how old is earth`
* SQL
  ```sql
  SELECT age FROM solar_system WHERE name = 'earth'
  ```
  * SQL 키워드는 대소문자를 구분하지 않음
    * 하지만 대문자로 작성하는 것을 권장(명시적으로 구분)
  * 각 SQL Statements의 끝에는 세미콜론(;)이 필요
    * 세미콜론은 각 SQL Statements을 구분하는 방법
  
# 2. SQL Statements
* **SQL 언어를 구성하는 가장 기본적인 코드 블록**
```sql
SELECT column_name FROM table_name; 
```
  * 해당 예시 코드는 SELECT Statement(SELECT 문)
  * 이 Statement는 SELECT, FROM 2개의 keyword로 구성 됨
## SQL Statements 유형
* 데이터베이스에서 수행 목적에 따라 대체로 4가지 범주로 나뉨

|유형|역할|SQL 키워드|
|:-:|:-:|:-:|
|DDL<br>(Data Definition Language|데이터 정의<br>데이터의 기본 구조 및 형식 변경|CREATE<br>DROP<br>ALTER|
|DQL<br>(Data Query Language)|데이터 검색|SELECT|
|DML<br>(Data Manipulation Language|데이터 조작<br>(추가, 수정, 삭제)|INSERT<br>UPDATE<br>DELETE|
|DCL<br>(Data Control Language)|데이터 및 작업에 대한<br>사용자 권한 제어|COMMIT<br>ROLLBACK<br>GRANT<br>REVOKE|

# 정리
* SQL은 데이터베이스와 상호 작용하고  \
데이터베이스에서 데이터를 반환하기 위한 언어
* 단순히 SQL 문법을 암기하고 상황에 따라 실행만 하는 것이 아닌  \
SQL을 통해 관계형 데이터베이스를 잘 이해하고 다루는 방법을 학습

# 용어
* Query
  * 질의, 질문
  * "데이터베이스로부터 정보를 요청"하는 것
  * 일반적으로 SQL로 작성하는 코드를 쿼리문(SQL문)이라 함
* SQL 표준
  * SQL은 미국 국립 표준 협회(ANSI)와 국제 표준화 기구(ISO)에 의해 표준이 채택됨
  * 널리 사용되는 모든 RDBMS에서 SQL 표준을 지원
  * 다만 **RDBMS별로 독자적인 기능에 따라 표준을 벗어나는 문법이 존재하니 주의**