# 딕셔너리(Dictionary)
## 목차
1. 해시 테이블
2. 딕셔너리 기본 문법
3. 딕셔너리 메서드
## 학습 목표
* 리스트와 딕셔너리의 특징과 시간 복잡도를 비교할 수 있다.
* 딕셔너리를 사용해야 하는 문제를 판별할 수 있다.
* 딕셔너리에 값을 추가, 삭제, 수정, 조회할 수 있다.
* 딕셔너리 주요 메서드를 활용할 수 있다.
# 1. 해시 테이블
* 해시 함수 : 임의 길이의 데이터를 고정 길이의 데이터로 매핑하는 함수
* 해시 : 해시 함수를 통해 얻어진 값
## 파이썬의 딕셔너리(Dictionary의 특징)
* 해시 함수와 해시 테이블을 이용하기 때문에  \
삽입, 삭제, 수정, 조회 **연산의 속도가 리스트보다 빠르다.**
  * *Hash function을 이용한 산술 계산으로 값이 있는 위치를 바로 알 수 있기 때문에*
* 딕셔너리와 리스트의 연산 시간 복잡도

|연산 종류|딕셔너리|리스트|
|:-:|:-:|:-:|
|Get Item|O(1)|O(1)|
|Insert Item|O(1)|O(N)|
|Update Item|O(1)|O(1)|
|Delete Item|O(1)|O(N)|
|Search Item|O(1)|O(N)|

### 딕셔너리는 언제 사용 해야할까?
* Key, Velue 구조로 관리를 해야 하는 경우(순서나 인덱스가 아닌 경우)
* 데이터에 대한 빠른 접근 탐색이 필요한 경우

# 2. 딕셔너리 기본 문법
* 선언
  * `변수 = {key1: value1, key2:value2, ...}`
  * `변수 = {}`
  * `변수 = dict()`
* 삽입/수정
  * `딕셔너리[key] = value`
* 삭제
  * `딕셔너리.pop(key,default)`
* 조회
  * `딕셔너리[key]`
  * `딕셔너리.get(key,default)`

# 3. 딕셔너리 메소드
* .keys()
  * 딕셔너리의 **key 목록**이 담긴 dict_keys 객체 반환
* .values()
  * 딕셔너리의 **value 목록**이 담긴 dict_values 객체 반환
* .items()
  * 딕셔너리의 **(key, value)**쌍 목록이 담긴 dict_items 객체 반환


[Counter 라이브러리](https://docs.python.org/ko/3/library/collections.html#collections.Counter)