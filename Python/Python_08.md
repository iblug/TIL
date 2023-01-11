# 사용자 정의 클래스
# 학습 목표
* 절차지향프로그래밍과 객체지향프로그래밍의 차이를 설명할 수 있다.
* 클래스와 인스턴스의 차이를 비교하고 설명할 수 있다.
* 클래스를 직접 정의하고 인스턴스를 생성할 수 있다.
* 인스턴스 속성을 활용하고 메서드를 조작할 수 있다.
# 객체 지향 프로그래밍
* 객체(object)의 특징
  * 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능한가?
  * 속성(attribue) : 어떤 상태(데이터)를 가지는가?
  * 조작법(method) : 어떤 행위(함수)를 할 수 있는가?
* 객체지향 프로그래밍이란?
  * 프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍 방법
  * *데이터와 기능(메소드) 분리, 추상화된 구조(인터페이스)*
```py
# 객체지향 프로그래밍
# ex) 사각형 넓이와 둘레

class Rectangle:              # 클래스(class)
  def __init__(self, x, y):   # 사각형의 정보 : 속성(attribute)
    self.x = x              # 각 변의 길이 x, y
    self.y = y

  def area(self):             # 메소드(method)
    return self.x * self.y  #넓이

  def circumference(self):    # 메소드(method)
    return 2 * (self.x + self.y)# 둘레

r1 = Rectangle(10, 30)      # 인스턴스(instance) 
r1.area()
r1.circumference()

r2 = Rectangle(300, 200)     # 인스턴스(instance)
r2.area()
r2.circumference()
```
# 객체지향의 장점
* **프로그램을 유연하고 변경이 용이하게** 만들기 때문에 대규모 소프트웨어 개발에 많이 사용됨.
* 프로그래밍을 더 배우기 쉽게 하고 **소프트웨어 개발과 보수를 간편하게** 하며, 보다 **직관적인 코드 분석을 가능하게** 함

# 클래스
```py
# 클래스 정의
class MyClass:
  pass
# 인스턴스 생성
my_instance = MyClass()
# 메서드 호출
my_instance.my_method()
# 속성
my_instance.my_attribute
```
* 클래스(class) : 객체들의 분류
* 인스턴스(instance) : 하나하나의 실체
* 속성 : 특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터를 의미
* 메소드 : 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)

# 인스턴스
* 인스턴스 변수
  * 인스턴스가 개인적으로 가지고 있는 속성(attribute)
  * 각 인스턴스들의 고유한 변수
* 생성자 메소드에서 `self.<name>`으로 정의
* 인스턴스가 생성된 이후 `<instance>.<name>`으로 접근 및 할당
* 인스턴스 메소드
  * 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메소드
  * 클래스 내부에 정의되는 메소드의 기본
  * 호출 시, 첫번째 인자로 인스턴스 자기자신(self)이 전달됨
* self
  * 인스턴스 자기자신
  * 파이썬에서 인스턴스 메소드는 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계
    * 매개변수 이름으로 `self`를 첫번째 인자로 정의
    * 다른 단어로 써도 작동하지만, 파이썬의 암묵적인 규칙
* 생성자(constructor) 메소드
  * 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드
  * 인스턴스 변수들의 초기값을 설정
    * 인스턴스 생성
    * `__init__` 메소드 자동 호출
* 소멸자(destructor) 메소드
  * 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 메소드
  * *프로그램이 끝나면 자동으로 인스턴스가 삭제됨*
* 매직 메소드(스페셜 메소드)
  * Double underscore(`__`)가 있는 메소드는 특수 동작을 위해 만들어진 메소드
  * 특정 상황에 자동으로 불리는 메소드
  * 객체의 특수 조작 행위를 지정(함수, 연산자 등)
  * 예시
    * `__str__(self)`, `__len(self)__`, `__repr__(self)`
    * `__lt__(self, other)`, `__le__(self, other)`, `__eq__(self, other)`
    * `__gt__(self, other)`, `__ge__(self, other)`, `__ne__(self, other)`
      * `__str__` : 해당 객체의 출력 형태를 지정
        * 프린트 함수를 호출할 때, 자동으로 호출
        * 어떤 인스턴스를 출력하면 \_\_str\_\_의 return 값이 출력
      * `__gt__` : 부등호 연산자(>, greater than)
```py
class Person:
  def __init__(self, name, age): # 생성자(constructor)
    self.name = name # 인스턴스 변수 정의
    self.age = age

  def __del__(self):        # 소멸자(destructor)
    print(f'\'{self}\' 인스턴스가 사라졌습니다.')

  def __str__(self):
    return self.name
  
  def __gt__(self, other):
    if self.age > other.age:
      return self
    else:
      return other

  def greeting(self):       # 인스턴스 메소드
    return f'{self.name} 입니다.'

p1 = Person('홍길동', 21) # 인스턴스 변수 접근 및 할당
print(p1.name) # 홍길동

p1.name = '철수'
print(p1.name) # 철수

p2 = Person('영희', 20)

print(p2) # 영희
print(p1 < p2) # 철수

del p2 # '영희' 인스턴스가 사라졌습니다.

# '철수' 인스턴스가 사라졌습니다. # 프로그램이 끝나면 자동으로 인스턴스가 삭제됨
```