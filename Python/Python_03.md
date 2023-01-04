# Python_03_funcion
# 학습 목표
* 함수를 사용해야 하는 이유를 알고 설명할 수 있다.
* 파이썬 내장 함수를 활용하여 코드를 작성할 수 있다.
* 함수별 인자와 return(반환)을 구분할 수 있다.

# 함수(function)
* *추상적 개념(Abstraction)*의 함수
  * 사물이 지니고 있는 여러 가지 측면 가운데서 특정한 측면만을 가려내어 포착하는 것
  * 복잡한 내용을 숨기고, 기능에 집중하여 사용할 수 있음.
    * **재사용성, 가독성, 생산성**
* 분해성(Decomposition)
  * 기능을 분해, 재사용 가능
* **함수의 정의**
  * **특정한 기능을 하는 코드의 조각**(묶음)
  * 특정 명령을 수행하는 코드를 매번 다시 작성하지 않고, **필요 시에만 호출**하여 간편히 사용
* 함수를 배우는 이유
  * **코드 중복 방지**
  * **재사용 용이**
* 함수 기본 구조
  * 선언과 호출(define & call)
  * 입력(Input)
  * 범위(Scope)
  * 결과값(Output)

## 사용자 함수(Custom Function)
* 구현되어 있는 함수가 없는 경우, **사용자가 직접 함수를 작성 가능**
  ```py
  def funcion_name
      # code block
      return returning_value
  ```

## 내장 함수(Built-in Function)
* Pyehon에서 미리 구현해 놓은 함수
  * 내장 함수가 적혀있는 [공식 문서](https://docs.python.org/ko/3/library/functions.html)
    * *공식 문서 이해하고 분석하기(2:09:00~)*
* 자주 사용하는 함수 *(무엇을 반환하는 지 기억하자!!)*
  * len(s)
    * 객체의 길이를 반환
  * sum(iterable, start=0)
    * 합계를 반환
  * max(iterable) / min(iterable)
    * 가장 큰 값 / 가장 작은 값 을 반환
    * 중복이면 처음 만남 항목을 반환
* 수학 관련 함수
  * abs(x)
    * 절댓값을 반환
  * divmod(a, b)
    * a를 b로 나눈 몫, 나머지를 반환
    * 튜플형으로 반환(q, r)
      ```py
      a = divmod(10, 3)
      print(a) # (3, 1)
      print(type(a)) # <class 'turple'>
      ```
  * pow(base, exp, mod=None)
    * base의 exp 거급제곱을 반환
  * round(number, ndigit=None)
    * ndigit정밀도로 반올림한 값을 반환
    ```py
    a = 1234.5678
    print(round(a, 2)) # 1234.57 # float
    print(round(a, 0)) # 1235.0
    print(round(a)) # 1235 # int
    print(round(a, -2)) # 1200.0
    ```
* 논리 관련 함수
  * all(iterable)
    * 모든 요소가 참이면(또는 비어있으면) True를 반환
  * any(iterable)
    * 요소 중 어느 하나라도 참이면 True를 반환
    * 비어있으면 False를 반환
* 기타 함수
  * bin(x), oct(x), hex(x)
    * 정수를 "0b", "0o", "0x" 접두사가 붙은 이진, 8진수, 16진수 문자열로 반환
  * ord(c)
    * 유니코드 문자 c에 대응되는 유니코드 숫자로 반환
  * chr(i)
    * 유니코드 숫자가 정수 i에 대응되는 문자를 반환
  ```py
  f = 3
  print(bin(f), oct(f), hex(f))
  # 0b11111 0o37 0x1f
  print(ord('D')) # 68
  print(chr(70)) # F
  ```
* map(function, iterable)
  * 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function)적용하고,  \
  그 결과를 map object로 반환
  ```py
  n, m = map(int, input().split())
  # 3 5 입력

  print(n, m) # 3 5
  print(type(n), type(m)) # <class 'int'> <class 'int'>
  ```
