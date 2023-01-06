# Python 파일 입출력
# 학습 목표
* 파이썬을 활용하여 파일을 읽고 쓸 수 있다.
* JSON 형식의 파일을 읽고 활용할 수 있다.

## 파일 입력
* open(file, mode = 'r', encoding=None)
 * mode
  * `'r'` : 읽기
  * `'w'` : 쓰기
    * 해당 위치에 파일이 없을경우, 새 파일 생성
    * 해당 위치에 파일이 있을 경우, 기존 파일 내용이 사라짐
  * `'a'` : 추가
    * 파일의 마지막에 데이터 추가

## 파일 활용
* 파일 객체 활용
  * `.close()`를 반드시 호출하여 종료시켜야 오류가 발생하지 않음.
  ```py
  f = open('workfile', 'w', encoding='utf-8')
  read_data = f.read()
  #<Code..>
  f.close()
  ```
* with 키워드 활용
  * `.close()`가 없어도 문단이 끝나면 close됨
  ```py
  with open('workfile') as f:
      read_data = f.read()
  ```
## JSON
* 자바스크립트 객체 표기법
* 개발환경에서 많이 활용되는 데이터 양식
* 웹 어플리케이션에서 데이터를 전송할 때 일반적으로 사용함
* 문자 기반(텍스트) 데이터 포멧으로 다수 프로그래밍 환경에서 쉽게 활용 가능함
  * 텍스트를 언어별 데이터 타입으로 변환시키거나  \
  언어별 데이터 타입을 적절하게 텍스트로 변환
### JSON 파일의 활용
* 객체(리스트, 딕셔너리 등)를 JSON으로 변환
  * 객체를 JSON으로 변환
   ```py
   import json
   x = [1, 'simple', 'list']
   json.dumps(x)
   # '[1, "simple", "list"]
   ```
  * JSON을 객체로 변환
   ```py
   x = json.load(f)
   ```