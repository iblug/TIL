# 기타 함수
## 대소문자 구분
* 기본적으로 대소문자 구분 안함
* 구분하려면 BINARY

## NULL 치환
* IFNULL(컬럼명, 0)
  * 컬럼이 NULL이면 0
* IF(컬럼명 IS NULL, '1', '2')
  * 컬럼이 NULL일 경우 1을, NULL이 아닐때는 2
* NULLIF(A, B)
  * A == B 의 결과가 TRUE면 NULL, FALSE면 A
```sql
SELECT IFNULL(column1, '-') FROM table1;
SELECT IF(column1 IS NULL,'NONE', 'YES') FROM table1;
SELECT NULLIF(1,1);
-- NULL
SELECT NULLIF(1,2);
-- 1
```

## NULL COUNT
* NULL을 카운트 할때는 전체에서 NULL이 아닌것을 빼 줌
```SQL
COUNT(*)-COUNT(AGE)
```

## DATE 포멧 변경
* DATE_FORMAT(date, format)
```sql
SELECT DATE_FORMAT('20230305', '%Y/%m/%d')
-- 2023/03/05
SELECT DATE_FORMAT('20230305', '%Y/%m/%d')
-- 2023-03-05
SELECT DATE_FORMAT('20230305', '%Y %M %e %W')
-- 2023 March 5 Sunday
```
* [w3school-DATE_FORMAT](https://www.w3schools.com/sql/func_mysql_date_format.asp)
* [tistory](https://ponyozzang.tistory.com/656)

## 날짜 계산
[label](https://velog.io/%40donghoim/MySQL-%EC%8B%9C%EA%B0%84-%EB%8D%94%ED%95%98%EA%B8%B0-%EB%B9%BC%EA%B8%B0-DATEADD-DATESUB-%ED%95%A8%EC%88%98)
add, sub..

## 날짜 차이
[label](https://extbrain.tistory.com/78)
[label](https://ponyozzang.tistory.com/697)

## 반올림과 버림
[label](https://devjhs.tistory.com/87)

## 날짜 관련
[label](https://jang8584.tistory.com/7)