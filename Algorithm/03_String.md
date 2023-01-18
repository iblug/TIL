# 문자열(String)
## 목차
1. 문자열 조작
2. 문자열 메서드
3. 아스키(ASCII) 코드
## 학습 목표
* 문자열을 인덱스로 접근하고 슬라이싱을 할 수 있다.
* 문자열을 조작하는 유형을 알고 활용할 수 있다.
* 문자열 메서드와 그 결과를 설명할 수 있다.
# 1. 문자열 조작
## 문자열 슬라이싱
* s = 'abcdefghi'
  * *len(s) = 9*

  ||a|b|c|d|e|f|g|h|i|
  |:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
  |index|0|1|2|3|4|5|6|7|8|
  |index|-9|-8|-7|-6|-5|-4|-3|-2|-1|

  * s[2:5] = 'cde'
  * s[-6:-2] = 'defg'
  * s[2:5:2] = 'ce'
  * s[-6:-1:3] = 'dg'
  * s[2:5:-1] = ''
  * s[:3] = 'abc' = s[:-6] = s[:-len(s)+n]
  * s[5:] = 'fghi' = s[-4:] = s[len(s)-n-1:]
  * s[:] = 'abcdefghi'
  * s[::-1] = 'ihgfedcba'

- 정규 표현식(RE, Regex)
  * Regular Expression
  * [정리(tistory)](https://hamait.tistory.com/342)
  * [test하는 곳](https://regexr.com/)

# 2. 문자열 메서드
1. .split()
2. .strip()
3. .find()
4. .index()
5. .count()
6. .replace()
7. .join()

* 메서드 안쓰고 구현해보기

## 1. .split(`기준 문자`)
* 문자열을 일정 **기준**으로 나누어 **리스트로 반환**
* default = `' '`
  * *괄호 안에 아무것도 넣지 않으면 자동으로 공백을 기준으로 설정*
## 2. .strip(`제거할 문자`)
* 문자열의 **양쪽** 끝에 있는 특정 문자를 모두 **제거**한 새로운 문자열 반환
* default = `' '`
* 제거할 문자를 여러 개 넣으면 해당하는 모든 문자들을 제거
```py
word = " Hello World "
print(word.strip())
# Hello World

word = "aHello Worlda"
print(word.strip('a'))
# Hello World

word = "Hello World"
print(word.strip('Hd'))
# ello Worl

word = "Hello Worldddddd"
print(word.strip('d'))
# Hello Worl
```

## 3. .find(`찾는 문자`)
* 특정 문자가 처음으로 나타나는 **위치(인덱스)**를 반환
* 찾는 문자가 없다면 `-1`을 반환
## 4. .index(`찾는 문자`)
* 특정 문자가 처음으로 나타나는 **위치(인덱스)**를 반환
* 찾는 문자가 없다면 **오류** 발생
## 5. .count(`개수를 셀 문자`)
* 문자열에서 특정 문자가 **몇 개**인지 반환
* 문자 뿐만 아니라, 문자열의 개수도 확인 가능
## 6. .replace(`기존문자`, `새로운 문자`)
* 문자열에서 기존 문자를 새로운 문자로 **수정**한 새로운 문자열 반환
* 특정 문자를 빈 문자열(`''`)로 수정하여 마치 해당 문자를 **삭제한 것 같은 효과 가능**
* 사용할 때 주의
  * 반복문에서 두 번 이상 반복 될 경우!
## 7. `삽입할 문자`.join(iterable)
* iterable의 **각각 원소 사이에 특정 문자를 삽입**한 새로운 문자열 반환
* 공백 출력, 콤마 출력 등 **원하는 출력 형태**를 위해 사용
## 8. 기타 메서드
* `.startswith('')`, `.endswith('')` 등 ...
* [w3schools](https://www.w3schools.com/python/python_ref_string.asp)

# 3. 아스키(ASCII) 코드
* 미국 정보교환 표준부호(American Standard Code for Information Interchange)
* 알파벳을 표현하는 대표 인코딩 방식
* 각 문자를 표현하는데 1byte(8bits) 사용
  * 1bit : 통신 에러 검출용
  * 7bit : 문자 정보 저장 (총 128개)
* `ord(<문자>)`
  * **문자 -> 아스키코드**로 변환하는 내장함수
* `chr(<아스키코드>)`
  * **아스키코드 -> 문자**로 변환하는 내장함수

- 기타 참고
  - 이모지
  - cp949 euc-kr
  - 유니코드
  - [링크](https://docs.python.org/ko/3/howto/unicode.html)