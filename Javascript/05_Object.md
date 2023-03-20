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

# 3. 객체와 함수
## Method
* 객체 속성에 정의된 함수
  ```js
  const person = {
    name: 'Sophia'
    greeting: function () {
      return 'Hello'
    },
  }

  // greeting 메서드 호출
  console.log(person.greeting()) // Hello
  ```
* 'this' 키워드를 사용해 객체에 대한 특정한 작업을 수행 할 수 있음
  ```js
  const person = {
    name: 'Sophia', 
    greeting: function () {
      return `Hello my name is ${this.name}`
    },
  }

  // greeting 메서드 호출
  console.log(person.greeting()) // Hello my name is Sophia
  ```

## this
* 함수나 메서드를 호출한 객체를 가리키는 키워드
  * 함수 내에서 객체의 속성 및 메서드에 접근하기 위해 사용
* JS에서 this는 함수를 **호출하는 방법**에 따라 가리키는 대상이 다름
  * 단순 호출 시 -> 전역 객체
    ```js
    const myFunc = function () {
      return this
    }

    console.log(myFunc()) // window
    ```

  * 메서드 호출 시 -> 메서드를 호출한 객체
    ```js
    const myObj = {
      data: 1, 
      myFunc: function () {
        return this
      }
    }

    console.log(myObj.myFunc()) // myObj
    ```
* Nested 함수에서의 문제점과 해결책
  * 문제점: forEach의 인자로 들어간 함수는 일반 함수 호출이기 때문에 this가 전역 객체를 가리킴
    ```js
    const myObj2 = {
      numbers: [1, 2, 3],
      myFunc: function () {
        this.nembers.forEach(function (number) {
          console.log(number) // 1 2 3
          console.log(this) // window
        })
      }
    }
    ```
  * 해결책: **화살표 함수**는 자신만의 this를 가지지 않기 때문에 외부 함수에서 this값을 가져옴
    ```js
    const myObj3 = {
          numbers: [1, 2, 3],
          myFunc: function () {
            this.numbers.forEach((number) => {
              console.log(number) // 1 2 3
              console.log(this) // myObj3
            })
          }
        }
    ```
# 99.참고
## 유용한 객체 메서드
```js
const profile = {
  name: 'Sophia'
  age: 30
}

console.log(Object.keys(profile)) // ['name', 'age']
console.log(Object.values(profile)) // ['Sophia', 30]
```
## JavaScript 'this' 특징
* JavaScript에서 this는 함수가 "호출되는 방식"에 따라 결정되는 현재 객체를 나타냄
* Python의 self와 Java의 this는 선언 시 값이 이미 정해지는 것에 비해 JavaScript의 this는 함수가 호출되기 전까지 값이 할당되지 않고 호출 시에 결정됨 (동적)

## JSON(JavaScript Object Notation)
* Key-Value 형태로 이루어진 자료 표기법
* JavaScript의 Object와 유사한 구조를 가지고 있지만 JSON은 형식이 있는 "문자열"
* JavaScript에서 JSON을 사용하기 위해서는 Object자료형으로 변경해야 함
* JSON <-> Object 변환하기
  ```js
  const jsObject = {
    coffee: 'Americano',
    iceCream: 'Cookie and cream',
  }
  ```
  ```js
  // Object -> JSON

  const objToJson = JSON.stringify(jsObject)

  console.log(objToJson) // {"coffee":"Americano","iceCream":"Cookie and cream"}
  console.log(typeof objToJson) // string
  ```
  ```js
  // JSON -> Object

  const jsonToObj = JSON.parse(objToJson)

  console.log(jsonToObj) // {coffee: 'Americano', iceCream: 'Cookie and cream'}
  console.log(typeof jsonToObj) // object
  ```