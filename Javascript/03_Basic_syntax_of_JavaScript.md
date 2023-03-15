# Basic syntax of JavaScript
## 목차
1. 개요
2. 변수
3. 데이터 타입
4. 연산자
5. 조건문
6. 반복문
## 학습 목표
* 변수 키워드에 따라 적절히 값을 할당하여 다양한 데이터를 다룰 수 있다.
* 연산자를 활용하여 다양한 계산을 수행할 수 있다.
* if-else문을 활용하여 조건에 따라 다른 동작을 수행할 수 있도록 한다.
* for문, while문 등 다양한 반복문을 사용하여 반복적인 작업을 수행할 수 있다.

# 1. 개요
* 본 교재는 ECMAScript 2015 (ES6) 이후의 명제를 따름
  * JavaScript는 ECMAScript 명세에 서술된 모든 기능을 지원함
* 코딩 스타일 가이드
  * [https://standardjs.com/rules-kokr.html](https://standardjs.com/rules-kokr.html)

# 2. 변수
## 식별자(변수명) 작성 규칙
* 반드시 문자, 달러($) 또는 밑줄(_)로 시작
* 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작
* 예약어 사용 불가
  * for, if, function 등
* 카멜 케이스 (camelCase)
  * 변수, 객체, 함수에 사용
* 파스칼 케이스(PascalCase)
  * 클래스, 생성자에 사용
* 대문자 스네이크 케이스(SNAKE_CASE)
  * 상수(constants)에 사용
  * 상수: 개발자의 의도와 상관없이 변경될 가능성이 없는 값
  * 상수 상수 상수 상수 
## 변수 선언 키워드
1. let
* 블록 스코프를 갖는 지역 변수를 선언
* 재할당 가능 & 재선언 불가능
2. const
* 블록 스코프를 갖는 지역 변수를 선언
* 재할당 불가능 & 재선언 불가능
* 선언 시 반드시 초기값 설정 필요
### 블록 스코프 (block scope)
* if, for, 함수 등의 **중괄호(`{ }`)내부**를 가리킴
* 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능
### 변수 선언 키워드 정리
* 기본적으로 const 사용을 권장
* 재할당해야 하는 경우만 let을 사용
* 다만, 실습에서는 편의를 위해 재할당이 가능한 let을 기본적으로 사용

# 3. 데이터 타입
## 분류
|원시 자료형|참조 자료형|
|:-:|:-:|
|Primitive type|Reference type|
|Number, String, Boolean, undefined, null|Objects(Object, Array, Function)|
|변수에 **값**이 직접 저장되는 자료형 (불변, 값이 복사)|객체의 **주소**가 저장되는 자료형 (가변, 주소가 복사)|
* 원시 자료형
  ```js
  const bar = 'baz'
  console.log(bar) // baz

  bor.toUpperCase()
  console.log(bar) // baz

  let a = 10
  let b = 
  b = 20
  console.log(a) // 10
  console.log(b) // 20
  ```
* 참조 자료형
  ```js
  // 참조 자료형
  const obj1 = { name: 'Alice', age: 30 }
  const obj2 = obj1
  obj2.age = 40
  console.log(obj1.age) // 40
  console.log(obj2.age) // 40
  ```

### Number
* 정수 또는 실수형 숫자를 표현하는 자료형
```js
const a = 13
const b = -5
const c = 3.14 // float - 숫자표현
const d = 2.998e8 // 2.998 * 10^8 = 299,800,000
const e = Infinity
const f = -Infinity
const g = NaN // Not a Number
```
### String
* 문자열
* 곱셈, 나눗셈, 뺄셈은 안되지만 덧셈을 통해 문자열끼리 붙일 수 있음
  ```js
  const firstName = 'Tony'
  const lastName = 'Stark'
  const fullName = firstName + lastName
  ```
* "**Template Literal**"을 사용하여 문자열 사이에 변수 삽입가능
  ```js
  const age = 10
  const massage = `홍길동은 ${age}세 입니다.`
  ```
  * ` `` `, `&{ }` 사용

### null
* 변수의 값이 없음을 **의도적**으로 표현할 때 사용
```js
const lastName = null
console.log(lastName) // null
```
### undefined
* 변수 선언 이후 직접 값을 할당하지 않으면 자동으로 할당됨
```js
let firstName
console.log(firstName) // undefined
```
#### null 과 undifined
* 동일한 역할을 하는 이 두개의 키워드가 존재하는 이유는 단순한 **JavaScript의 설계 실수**
* null이 원시 자료형임에도 불구하고 object로 출력되는 이유는 JavaScript 설계 당시의 버그를 해결하지 못한 것
  * 이미 null 타입에 의존성을 띄고 있는 많은 프로그램들이 망가질 수 있기 때문 (하위 호환 유지)
```js
typeof null // "object"
typeof undefined // "undefined"
```
## Boolean
* true와 false
* 조건문 또는 반복문에서 boolean이 아닌 데이터 타입은 자동 형변환 규칙에 따라 true 또는 false로 변환됨
* ToBoolean Conversions (자동 형변환)

  | 데이터 타입 | false | true |
  |:-:|:-:|:-:|
  | undefined | 항상 false | X |
  | null| 항상 false | X |
  | Number| 0, -0, NaN | 나머지 모든 경우 |
  | String | 빈 문자열 | 나머지 모든 경우 |
