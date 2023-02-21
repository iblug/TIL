# SQL - Advanced
## 목차
1. Transactions
2. Triggers
## 학습 목표
* Transaction을 사용하여 데이터베이스 일관성을 보장할 수 있다.
* Trigger 작동 방식을 이해하고 작성하여 데이터 무결성을 보장할 수 있다.

# 1. Transactions
* 여러 쿼리문을 묶어서 하나의 작업처럼 처리하는 방법
  * *(다 성공하던지 혹은 다 실패하던지 해야하는)*
* ex) 계좌이체 (인출 & 입금)
  * 송금 중에 알 수 없는 문제로 인출에는 성공했는데 입금에 실패한다면..?
  * 인출과 입금 모두 성공적으로 끝나야 거래가 최종 승인되고,  \
  중간에 문제가 발생한다면 거래를 처음부터 없었던 거래로 만들어야 함
  * 결국 함께 성공하던지 실패해야함
* 임시 데이터 영역에서 작업됨
* 쪼개질 수 없는 업무처리의 단위
* 전체가 수행되거나 또는 전혀 수행되지 않아야 함(All or Nothing)

## Transaction Syntax
```sql
START TRANSACTION
state_ments;
...
[ROLLBACK|COMMIT];
```
* `START TRANSACTION`
  * 트랜잭션 구문의 시작을 알림
* `COMMIT`
  * 모든 작업이 정상적으로 완료되면 한꺼번에 DB에 반영
* `ROLLBACK`
  * 부분적으로 작업이 실패하면 트랜잭션에서 진행한 모든 연산을 취소하고 트랜잭션 실행 전으로 되돌림

# 2. Triggers
* 특정 이벤트에 대한 응답으로 자동으로 실행되는 것
  * INSERT, UPDATE, DELETE

## Triggers Syntax
```sql
CREATE TRIGGER trigger_name
  {BEFORE | AFTER} {INSERT | UPDATE | DELETE}
  ON table_name FOR EACH ROW
  trigger_body;
```
* `CREATE TRIGGER` 키워드 다음에 생성하려는 트리거의 이름을 지정
* 각 레코드의 어느 시점에 트리거가 실행될지 지정(삽입, 수정, 삭제 전/후)
* ON 키워드 뒤에 트리거가 속한 테이블의 이름을 지정
* 트리거가 활성화될 때 실행할 코드를 trigger_body에 지정
  * 여러 명령문을 실행하려면 `BEGIN`, `END` 키워드로 묶어서 사용
```sql
-- Triggers practice #1
DELIMITER //
CREATE TRIGGER trigger_name
  BEFORE UPDATE
  ON articles FOR EACH ROW
BEGIN
  SET NEW.updatedAt = CURRENT_TIME();
END//
DELIMITER ;
```
* `DELIMITER` 
  * SQL의 구문 문자(`;`)를 변경
  * `BEGIN`-`END` 구문 사이에 여러 SQL 문이 작성되기 때문에 하나의 트리거로써 작동될 수 있도록 사용
* `BEGIN`-`END`
  * 하나 이상의 구문 목록을 표현
  * `BEGIN`-`END` 키워드로 둘러싸는 다중 구문을 구성하게 됨
* `OLD`, `NEW`
  * 트리거에서 특점 시점 전/후의 값에 접근할 수 있도록 제공하는 키워드
  * 상황별로 사용할 수 있는 여부
  
  ||OLD|NEW|
  |:-:|:-:|:-:|
  |INSERT|NO|YES|
  |UPDATE|YES|YES|
  |DELETE|YES|NO|

## 99. 참고
* Triggers 관련 추가 명령문
```sql
-- 트리거 목록 확인
SHOW TRIGGERS;

-- 트리거 삭제
DROP TRIGGER trigger_name;
```
* Triggers 생성 시 에러 해결
  * 트랜잭션 생성 후 정상 적으로 종료되지 않아 발생하는 에러 발생 시 해결법
  * Error Code:2013. Lost connection to MySQL server during query
  * Error Code:2015. Lock wait timeout exceeded; try restarting transacion
```sql
-- 실행중인 프로세스 목록 확인
SELECT * FROM information_schema.INNODB_TRX;

-- 특정 프로세스의 trx_mysql_thread_id 삭제
KILL [trx_mysql_thread_id1];
```