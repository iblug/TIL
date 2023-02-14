# SQL - Managing Tables

## 목차
1. Create a table
2. Delete a table
3. Modifiying table fields

## 학습 목표
* CREATE와 DROP 문을 사용해 데이터베이스 테이블을 생성 및 삭제 할 수 있다.
* MySQL의 데이터 타입 및 제약 조건을 사용하여 요구사항에 맞는 스키마를 작성 할 수 있다.

# 1. Create a table
* 테이블 생성

## CREATE TABLE syntax
```sql
CREATE TABLE table_name (
  column_1 data_type, 
  column_2 data_type,
  ...,
  constraints
);
```
  * 각 필드에 적용할 데이터 타입(data type) 작성
  * 테이블 및 필드에 대한 제약조건(constraints) 작성
* Table 구조 확인
```sql
SHOW COLUMNS FROM examples;
```

## 제약 조건(Constraint)
* 데이터 **무결성**을 지키기 위해 데이터를 입력 받을 때 실행하는 검사 규칙
  * *무결성: 데이터의 정확성과 일관성을 보증*
* 대표적인 MySQL Constraints
  * PRIMARY KEY: 해당 필드를 기본 키로 지정
  * NOT NULL: 해당 필드에 NULL 값을 저장하지 못하도록 지정

## AUTO_INCREMENT attribute
* 테이블의 기본 키에 대한 번호 자동 생성
* 특징
  * 기본 키 필드에 사용
    * 고유한 숫자를 부여
  * 시작 값은 1이며 데이터 입력 시 값을 생략하면 자동으로 1씩 증가
  * 이미 사용한 값을 재사용하지 않음
  * 기본적으로 NOT NULL 제약 조건을 포함

# 2. Delete a table
* 테이블 삭제
## DROP TABLE syntax
```sql
DROP TABLE table_name;
```
  * DROP TABLE statement 이후 삭제할 테이블 이름 작성

# 3. Modifying table fields
## ALTER TABLE statement
* 테이블 필드 조작(생성, 수정, 삭제)
  * ALTER TABLE **ADD** : 필드 추가
  * ALTER TABLE **MODIFY** : 필드 속성 변경
  * ALTER TABLE **CHANGE COLUMN** : 필드 이름 변경
  * ALTER TABLE **DROP COLUMN** : 필드 삭제
  
### ADD
```sql
ALTER TABLE
  table_name
ADD
  new_column_name column_definition;
```
  * ADD 키워드 이후 추가하고자 하는 새 필드 이름과 데이터 타입 및 제약 조건 작성
  
### MODIFY
```sql
ALTER TABLE
  table_name
MODIFY
  column_name column_definition;
```
  * MODIFY 키워드 이후 변경하고자 하는 필드 이름  \
  그리고 데이터 타입 및 제약 조건 작성
  
### CHANGE COLUMN
```sql
ALTER TABLE
  table_name
CHANGE COLUMN
  original_name new_name column_definition;
```
  * CHANGE COLUMN 키워드 이후  \
  기존 필드 이름, 변경하고자 하는 필드 이름, 데이터 타입 및 제약조건 작성

### DROP COLUMN
```sql
ALTER TABLE
  table_name
DROP COLUMN
  column_name;
```
  * DROP COLUMN 키워드 이후 삭제하고자 하는 필드 이름 작성

# 99. 참고
## 반드시 NOT NULL 제약을 사용해야 할까
* 'NO'
* 데이터베이스를 사용하는 프로그램에 따라 NULL을 저장할 필요가 없는 경우가 많으므로 되도록 NOT NULL로 정의
* '값이 없다.'라는 표현을 테이블에 기록하는 것은 0이나 빈 문자열 등을 사용하는 것으로 대체하는 것을 권장