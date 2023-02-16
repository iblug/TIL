# SQL - Nested Queries
## 목차
1. Introduction to Subquery
2. Conditional Statements

## 학습 목표
* SQL subquery가 무엇인지 이해하고, 조건에 따라 하나 이상의 테이블에서 데이터를 검색할 수 있다.
* SWLECT, FROM, WHERE 절 등 다양한 맥락에서 사용하는 subquery를 작성할 수 있다.

# 1. Introduction to Subquery
## Subquery
* 단일 쿼리문에 여러 테이블의 데이터를 결합하는 방법
* 특징
  * 조건에 따라 하나 이상의 테이블에서 데이터를 검색하는 데 사용
  * SELECT, FROM, WHERE, HAVING 절 등에서 다양한 맥락에서 사용
* ex
```sql
DELETE FROM table1
WHERE age = (
  SELECT MIN(age) FROM table1
);
```
## EXISTS operator
* 쿼리 문에서 반환된 레코드의 존재 여부를 확인
* EXISTS syntax
```sql
SELECT
  select_list
FROM
  table
WHERE
  [NOT] EXISTS (subquery);
```
  * subquery가 하나 이상의 행을 반환하면 EXISTS 연산자는 true를 반환하고 그렇지 않으면 false를 반환
  * 주로 WHERE 절에서 subquery의 반환 값 존재 여부를 확인하는데 사용

2. Conditional Statements
## CASE statement
* 
* CASE syntax
```sql
CASE case_value
  WHEN when_value1 THEN statements
  WHEN when_value2 THEN statements
  ...
  [ELSE else-statements]
END CASE;
```
  * case_value가 when_value와 동일한 것을 찾을 때까지 순차적으로 비교
  * when_value와 동일한 case_value를 찾으면 해당 THEN 절의 코드를 실행
  * 동일한 값을 찾지 못하면 ELSE 절의 코드를 실행
    * ELSE 절이 없을 때 동일한 값을 찾지 못하면 오류 발생