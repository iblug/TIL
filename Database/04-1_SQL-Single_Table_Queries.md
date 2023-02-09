# SQL-Singel_Table_Queries

## 목차
1. Querying data
2. Sorting data
3. Filtering data
4. Grouping data

## 학습 목표
* 단일 테이블 내에서 SELECT문을 사용하여  \
테이블의 특정 결과를 반환할 수 있다.
* SELECT문과 함께 다양한 절을 사용해 쿼리 결과를  \
정렬 및 필터링 할 수 있다.
* GROUP BY와 Aggregation Function을 사용해 각 데이터 값에 대한 계산된 단일 값을 그룹화하여 반환할 수 있다.

# 1. Querying data
* **SELECT** statement: 테이블에서 데이터를 조회

## SELECT syntax
```sql
SELECT
  select_list
FROM
  table_name;
```
* SELECT 키워드 다음에 데이터를 선택하려는 필드를 하나 이상 지정
* FROM 키워드 다음에 데이터를 선택하려는 테이블의 이름을 지정

- ex5)테이블 orderdetails에서 productCode, 주문 총액 필드의 모든 데이터를 조회
  * (단, 주문 총액 필드는 quantityOrdered와 priceEach 필드를 곱한 결과 값)
```sql
SELECT
  productCode,
  quantityOrdered * priceEach AS '주문 총액'
FROM
  orderdetails;
```
  * **Arithmetic Operators**(기본적인 사칙연산 사용 가능)
  
## SELECT 정리
* SELECT 문을 사용하여 테이블의 데이터를 조회 및 반환
* SELECT * (asterisk)를 사용하여 테이블의 모든 필드 선택

# 2. Sorting data
* **ORDER BY** clause: 조회 결과의 레코드를 정렬

## ORDER BY syntax
```sql
SELECT
  select_list
FROM
  table_name
ORDER BY
  column1 [ASC|DESC],
  column1 [ASC|DESC],
  ...;
```
* FROM clause 뒤에 위치
* 하나 이상의 컬럼을 기준으로 결과를 오름차순, 내림차순으로 정렬할 수 있음
  * ASC: 오름차순(기본 값)
  * DESC: 내림차순
- ex3) 테이블 employees에서 lastName 필드를 기준으로 내림차순으로 정렬한 다음 firstName 필드 기준으로 오름차순 정렬하여 조회
```sql
SELECT
  lsatName, firstName
FROM
  employees
ORDER BY
  lastName DESC,
  firstName;
```

## SELECT statement 실행 순서<br>
> FROM > SELECT > ORDER BY<br>
1. 테이블에서(FROM)
2. 조회하여(SELECT)
3. 정렬(ORDER BY)