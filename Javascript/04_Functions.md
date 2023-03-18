# Functions
## 목차
1. 개요
2. 함수의 정의
## 학습 목표
1. 함수를 정의하는 방법과 함수를 호출하는 방법을 이해할 수 있다.
2. 함수를 선언식으로 정의하는 방법과 변수에 할당하는 표현식으로 정의하는 방법을 이해하고 활용할 수 있다.
3. 화살표 함수의 개념과 사용법을 이해하고 작성할 수 있다.
4. 함수를 사용해 코드를 모듈화하고 재사용성을 높일 수 있다.

# 1. 개요
* Function
  * 참조 자료형에 속하며, 모든 함수는 Funcion object
* 함수의 구조
  * 함수의 이름
  * 함수의 매개변수
  * 함수의 body를 구성하는 statement
  ```js
  function name ([param[, param, [..., param]]]) {
    statements
    return value
  }
  ```
    * return이 없다면 undefined를 반환

# 2. 함수의 정의

## 선언식(function declaration)
* syntax
  ```js
  function funcName () {
    statements
  }
  ```
* 예시
  ```js
  function add (num1, num2) {
    return num1 + num2
  }

  add(2, 7) // 9
  ```

## 표현식(function expression)
* syntax
  ```js
  const funcName = function () {
    statements
  }
  ```
* 예시
  ```js
  const sub = function (num1, num2) {
    return num1 - num2
  }
  sub(7, 2) // 5
  ```
* 함수 표현식 특징
  * 함수 이름이 없는 **'익명 함수'를 사용할 수 있음**
  * 선언식과 달리 표현식으로 정의한 함수는 **호이스팅 되지 않으**므로 코드에서 나타나기 전에 먼저 사용할 수 없음
    * Reference: Cannot access 'sub' before initialization
  * **사용 권장**

## 기본 함수 매개변수 (Default function parameter)
* 값이 없거나 undefined가 전달될 경우 이름 붙은 매개변수를 기본값으로 초기화
  ```js
  const greeting = function (name = 'Anonymous') {
    return `Hi ${name}`
  }

  greeting()  // Hi Anonymous
  ```
* 매개변수와 인자의 개수 불일치
  ```js
  // 매개변수 개수 < 인자 개수
  const noArgs = function () {
    return 0
  }

  noArgs(1, 2, 3) // 0

  const twoArgs = function (arg1, arg2) {
    retrun [arg1, arg2]
  }

  twoArgs(1, 2, 3) // [1, 2]

  // 매개변수 개수 > 인자 개수
  const threeArgs = function (arg1, arg2, arg3) {
    return [arg1, arg2, arg3]
  }

  threeArgs() // [undefined, undefined, undefined]
  threeArgs(1) // [1, undefined, undefined]
  threeArgs(2, 3) // [2, 3, undefined]
  ```
* 나머지 매개변수(Rest Parameters)
  * 무한한 수의 인자를 '배열'로 허용하여 가변 함수를 나타내는 방법
  ```js
  const myFunc = function (arg1, arg2, ...restArgs) {
    return [arg1, arg2, restArgs]
  }

  myFunc(1, 2, 3, 4, 5) // [1, 2, [3, 4, 5]]
  myFunc(1, 2) // [1, 2, []]
  ```
  * 함수 정의에는 하나의 나머지 매개변수만 있을 수 있음
  * 나머지 매개변수는 함수 정의에서 마지막 매개변수여야 함

## 화살표 함수 표현식(Arrow function expressions)
* 함수 표현식의 간결한 표현법
* 화살표 함수 표현식 작성 순서
1. function 키워드 제거 후 매개변수와 중괄호 사이에 화살표(=>) 작성
2. 함수의 매개변수가 하나 뿐이라면 매개변수의 `( )` 제거 가능
3. 함수 본문의 표현식이 한 줄이라면 `{ }`와 `return` 제거 가능
```js
const greeting = function (name) {
  return `hello, ${name}`
}

// 1. function 키워드 삭제 후 화살표 작성
const arrow1 = (name) => { 
  return `hello, ${name}` 
}

// 2. 인자가 1개일 경우에만 () 생략 가능
const arrow2 = name => { return `hello, ${name}` }

// 3. 함수 바디가 return을 포함한 표현식 1개일 경우에 {} & return 삭제 가능
const arrow3 = name => `hello, ${name}`
```

# 99. 참고
## 화살표 함수 표현식
```js
// 1. 인자가 없다면 () or _ 로 표시 가능
const noArgs1 = () => 'No args'
const noArgs2 = _ => 'No args'

// 2-1. object를 return 한다면 return을 명시적으로 작성해야 함
const returnObject1 = () => { return { key: 'value' } }

// 2-2. return을 적지 않으려면 소괄호로 감싸야 함
const returnObject = () => ({ key: 'value' })
```