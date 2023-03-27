# 클래스
* 클래스 속성(attribute)
  * 한 클래스의 모든 인스턴스라도 똑같은 값을 가지고 있는 속성
  * 클래스 선언 내부에서의 정의
  * `<classname>.<name>으로 접근 및 할당
* 클래스 메서드
  * 클래스가 사용할 메서드
  * @classmethod 데코레이터를 사용하여 정의
    * 데코레이터 : 함수를 어떤 함수로 꾸며서 새로운 기능을 부여
  * 호출 시, 첫 번째 인자로 클래스(cls)가 전달됨
  ```py
  class MyClass:

    @classmethod
    def class_method(cls, arg1, ...)
  ```
* 스태틱 메서드
  * 인스턴스나 클래스를 사용하지 않는 메서드
  * @staticmethod 데코레이터를 사용하여 정의
  * 호출 시, **어떠한 인자도 전달되지 않음**  \
  (클래스 및 인스턴스 정보에 접근/수정불가)
  ```py
  class MyClass

    @staticmethod
    def static_method(arg1, ...)
  ```
* 인스턴스와 클래스 간의 이름 공간(namespace)
  * 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
  * 인스턴스를 만들면, 인스턴스 객체가 생성되고 이름 공간 생성
  * 인스턴스에서 특정 속성에 접근하면, 인스턴스-클래스 순으로 탐색
  
# 상속
## 클래스 상속
* 상속
  * 두 클래스 사이 부모 - 자식 관계를 정립하는 것
    * 예) 모든 파이썬 클래스는 object를 상속 받음
* 부모에 정의된 속성이나 메서드를 활용하거나 오버라이딩(재정의)를 하여 활용
  * 코드의 재사용성을 높이고 클래스 간의 계층적 관계를 활용함
```py
class ChildClass(ParentClasss):
  pass
```
## 상속 관련 함수와 메서드
* isinstance(object, classinfo)
  * classinfo의 istance거나 subclass*인 경우 True
* issubclass(class, classinfo)
  * class가 classinfo의 subclass면 True
  * classinfo는 클래스 객체의 튜플일 수 있으며, classinfo의 모든 항목을 검사
* super()
  * 자식클래스에서 부모클래스를 사용하고 싶은 경우 활용

- 메서드 오버라이딩
  * 상속 받은 메서드를 재정의
    * 상속받은 클래스에서 같은 이름의 메서드로 덮어씀
    * 부모 클래스의 메서드를 실행시키고 싶은 경우 super를 활용
## 다중 상속
* 파이썬은 두개 이상의 클래스를 상속 받을 수 있음
* 상속 받은 모든 클래스의 요소를 활용 가능함
* 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정됨

# 파이썬 응용/심화
## 추가 문법
* 조건표현식(Conditional Expression)

  * `<True인 경우 값> if <expression> else <False 인 경우 값>`
  ```py
  num = -5
  value = num if num >= 0 else -num
  print(value) # 5

  num = 2
  result = '홀' if num % 2 else '짝'
  print(result) # 짝
  ```

* enumerate 순회
  * 인덱스와 객체를 쌍으로 담은 열거형(enumerate) 객체 반환
    * (index, value) 형태의 tuple로 구성된 열거 객체를 반환
  ```py
  members = ['민수', '영희', '철수']
  enumerate(members)
  # <enumerate at 0x105d3e100>
  list(enumerate(members))
  # [(0, '민수'), (1, '영희'), (2, '철수')]
  list(enumerate(members, start=1))
  # [(1, '민수'), (2, '영희'), (3, '철수')]
  ```

* List Comprehension / Dictionary Comprehension
  * `[<expression> for <변수> in <iterable>]`
  * `[<expression> for <변수> in <iterable> if <조건식>]`

  - `{key: value for <변수> in <iterable>}`
  - `{key: value for <변수> in <iterable> if <조건식>}`
  ```py
  cubic_list = [number**3 for number in range(1, 4)]
  print(cubic_list)
  # [1, 8, 27]

  cubic_dict = {number: number**3 for number in range(1, 4)}
  print(cubic_dict)
  ```
* lambda 함수
  * lambda [parameter] : 표현식
  * 표현식을 계산한 결과값을 반환하는 함수로, 이름이 없는 함수여서 익명함수라고도 불림
  * 특징
    * return문을 가질 수 없음
    * 간편 조건문 외 조건문이나 반복문을 가질 수 없음
  * 장점
    * 함수를 정의해서 사용하는 것보다 간결하게 사용 가능
    * def를 사용할 수 없는 곳에서도 사용 가능

    ```py
    # 3으로 나눈 나머지
    numbers = [1, 2, 3, 4, 5, 6, 7]
    print(list(map(lambda n: n % 3, numbers)))
    # [1, 2, 0, 1, 2, 0, 1]
    ```

# 파이썬 버전별 업데이트
* Type annotation
  * 동적 타입 언어인 파이썬에서각 변수(3.6+)/함수(3.5)마다 Type에 대한 설명을 덧붙임
  * 정적 타입으로 변경되는 것은 아니지만, IDE/텍스트 에디터를 통해 경고를 확인하고, 코드를 작성하는 과정에서 도움을 받을 수 있음
  * [링크](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
  ```py
  hello: str = 'hello world!'

  def add(x: int, y: int) -> int:
      return x + y

  result: int = add(7, 4)
  ```

- Positional-only parameters(위치 전용 매개변수)
  * 함수를 정의할 때 어떻게 호출해야 하는지를 함께 지정
  * [공식 문서](https://docs.python.org/3/whatsnew/3.8.html?highlight%3Dfunction%20argument%20positional#positional-only-parameters)
  * [PEP570](https://peps.python.org/pep-0570/)
  ```py
  def f(a, b, /, c, d, *, e, f): 
  # a, b는 위치만 c, d는 위치 및 키워드 모두 e, f는 키워드만
    print(a, b, c, d, e, f)
  
  f(1, 2, 3, d=4, e=5, f=6)
  # 1 2 3 4 5 6

  def f2(a, b, /, **kwargs):
      print(a, b, kwargs)

  f2(10, 20, a=1, b=2, c=3)
  # 10 20 {'a': 1, 'b': 2, 'c': 3}    
  ```