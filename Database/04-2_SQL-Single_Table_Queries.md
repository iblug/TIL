# SQL-Singel_Table_Queries
## 학습 목표
* 단일 테이블 내에서 SELECT문을 사용하여 테이블의 특정 결과를 반환할 수 있다.
* SELECT문과 함께 다양한 절을 사용해 쿼리 결과를 정렬 및 필터링 할 수 있다.
* GROUP BY와 Aggregation Function을 사용해 각 데이터 값에 대함 계산된 단일 값을 그룹화 하여 반환할 수 있다.

# 3. Filtering data
* 데이터를 필터링하여 중복 제거, 조건 설정 등 SQL Query를 제어하기
* Clause
  * DISTINCT
  * WHERE
  * LIMIT
* Operator
  * BETWEEN
  * IN
  * LIKE
  * Comparison
  * Logical

## DISTINCT clause
* 조회 결과에서 중복된 레코드를 제거
* DISTINCT syntax
```sql
SELECT DISTINCT
  select_list
FROM
  table_name;
```
  * SELECT 키워드 바로 뒤에 작성해야 함
  * SELECT DISTINCT 키워드 다음에 고유한 값을 선택하려는 하나 이상의 필드를 지정

## WHERE clause
* 조회 시 특정 검색 조건을 지정
* WHERE syntax
```sql
SELECT
  select_list
FROM
  table_name
WHERE
  search_condition;
```
  * FROM clause 뒤에 위치
  * search_condition은 비교연산자 및 논리연산자(AND, OR, NOT 등)를 사용하는 구문이 사용됨
    * 비교연산자(Comparison Operators)
      * =, >=, !=, IS, LIKE, IN, BETWEEN...AND
    * 논리연산자(Logical Operators)
      * AND(&&), OR(||), NOT(!)
- IN operator
  * 값이 특정 목록 안에 있는지 확인
* LIKE operator
  * 값이 특정 패턴에 일치하는지 확인 with Wildcards
    * '%': 0개 이상의 문자열과 일치하는지 확인
    * '_': 단일 문자와 일치하는지 확인
  * 정규표현식(RX)
## LIMIT clause
* 조회하는 레코드 수를 제한
* LIMIT syntax
```sql
SELECT
  select_list
FROM
  table_name
LIMIT [offset,] row_count;
```
  * LIMIT clause는 하나 또는 두 개의 인자를 사용(0 또는 양의 정수)
  * row_count는 조회할 최대 레코드 수를 지정

# 4. Grouping data
## GROUP BY clause
* 레코드를 그룹화하여 요약본 생성 with 집계 함수(Affregation Functions)
* 값에 대한 계산을 수행하고 단일한 값을 반환하는 함수
  * SUM, AVG, MAX, MIN, COUNT
* GROUP BY syntax
```sql
SELECT
  c1, c2, ..., cn, aggregate_function(ci)
FROM
  table_name
GROUP BY
  c1, c2, ..., cn;
```
  * FROM 및 WHERE 절 뒤에 배치
  * GROUP BY 절 뒤에 그룹화할 필드 목록을 작성
* ex
```sql
SELECT
	jobTitle, COUNT(*)
FROM
	employees
GROUP BY
	jobTitle;
```

* HAVING clause
  * 집계 항목에 대한 세부 조건을 지정
  * 주로 GROUP BY와 함께 사용되며 GROUP BY가 없다면 WHERE처럼 동작

# SELECT statement 실행 순서
> FROM > WHERE > GROUP BY > HAVING > SELECT > ORDER BY > LIMIT
1. 테이블에서(FROM)
2. 특정 조건에 맞춰(WHERE)
3. 그룹화 하고(GROUP BY)
4. 만약 그룹 중에서 조건이 있다면 맞추고(HAVING)
5. 조회하여(SELECT)
6. 정렬하고(ORDER BY)
7. 특정 위치의 값을 가져온다(LIMIT)
* 작성순서
> SELECT > FROM > WHERE > GROUP BY > HAVING > ORDER BY > LIMIT

## 99. 참고
### 정렬에서의 NULL
* MYSQL에서 NULL은 NULL이 아닌 값 앞에 위치
  * NULL 값이 존재할 경우 오름차순 정렬 시 결과에 NULL이 먼저 출력
  * WHERE ~ IS NOT NULL 등으로 처리 가능
