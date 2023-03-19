# Object
## 목차
1. 개요
2. 객체의 속성
3. 객체와 함수
## 학습 목표
* Object의 개념과 기본적인 사용 방법을 이해할 수 있다.
* Object의 속성(property)에 접근하는 방법을 작성할 수 있다.
* Object의 속성을 추가, 수정, 삭제하는 방법을 작성할 수 있다.
* Object의 메서드와 this 키워드를 사용하여 속성을 조작할 수 있다.

# 1. 개요
## Object
* *(plain)* Object
* 키로 구분된 데이터 집합(data collection)을 저장하는 자료형
* 객체의 구조
  * 중괄호를 이용해 작성
  * 중괄호 안에는 key: value 쌍으로 구성된 속성(property)를 여러 개를 넣을 수 있음
  * key는 문자형, value는 모든 자료형이 허용
  ```js
  const user = {
    name: 'Sophia',
    age: 30,
    'key with space': true,
  }
  ```
  * "traiing comma"
    * 속성을 추가, 삭제, 이동하기가 용이해짐

# 2. 객체의 속성
* Property 활용
  ```js
  // 조회 (점 표기법, 대괄호 표기법)
  console.log(user.age) // 30
  console.log(user['age']) // 30
  console.log(user['key with space']) // true

  // 추가
  user.address = 'korea'
  console.log(user) // {name: 'Sophia', age: 30, key with space: true, address: 'korea'}

  // 수정
  user.age = 20
  console.log(user.age) // 20

  // 삭제
  delete user.address
  console.log(user) // {name: 'Sophia', age: 20, key with space: true}
  ```

* property 존재 여부 확인 - "in"
  ```js
  console.log('age' in user) // true
  console.log('county' in user) // false
  ```

* 단축 property
  ```js
  const age = 30
  const address = 'korea'

  // const oldUser = {
  //   age: age,
  //   address: address,
  // }

  const newUser = {
    age,
    address
  }
  ```

* 계산된 property
  * 키가 대괄호 (`[ ]`)로 둘러싸여 있는 프로퍼티
  * 고정된 값이 아닌 변수 값을 사용할 수 있음
  ```js
  const product = prompt('물건 이름을 입력해주세요')
  const prefix = 'my'
  const suffix = 'property'

  const bag = {
    [product]: 5, 
    [prefix + suffix]: 'value'
  }

  console.log(bag) // {연필: 5, myproperty: 'value'}
  ```
