# Array
## 목차
1. 개요
2. 배열과 메서드
## 학습 목표
* 배열 요소에 접근하는 방법을 이해하고, 인덱스를 사용하여 배열 요소를 읽거나 쓸 수 있다.
* 배열의 길이(length) 속성을 이해하고 활용할 수 있다.
* JavaScript에서 제공하는 다양한 배열의 메서드와 속성을 이해하고 활용할 수 있다.
* 콜백함수 구조를 활용하여 배열의 모든 요소에 접근하거나 조건에 맞는 요소만 처리하는 반복을 작성하는 방법을 이해한다.

# 1. 개요
## Object
* 키로 구분된 데이터 집합(data collection)을 저장하는 자료형
* *순서가 없다*
## Array
* **순서**가 있는 데이터 집합(data collection)을 저장하는 자료구조
* 배열의 구조
  * 대괄호를 이용해 작성
  * length를 사용해 배열에 담긴 요소가 몇 개인지 알 수 있음
  * 배열 요소의 자료형엔 제약이 없음
  * 배열의 마지막 요소는 객체와 마찬가지로 쉼표로 끝날 수 있음
  ```js
  const fruits = ['apple', 'banana', 'coconut']
  
  console.log(fruits[0])
  console.log(fruits[1])
  console.log(fruits[2])

  console.log(fruits.lenth)
  ```
* 배열과 반복
  ```js
  // for
  for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i])
  }

  // for-of
  for (const fruit of fruits) {
    console.log(fruit)
  }
  ```
# 2. 배열과 메서드
| 메서드 | 기능 | 역할 |
|:-:|:-:|:-:|
| push / pop | 배열 끝 요소를 추가 또는 제거 | 요소 추가/제거 |
| unshift / shift | 배열 앞 요소를 추가 또는 제거 | 요소 추가/제거 |
| forEach | 인자로 주어진 함수(콜백함수)를 배열 요소 각각에 대해 실행 | 반복 |
| map | 배열 요소 전체를 대상으로 함수(콜백함수)를 호출하고, <br>함수 호출 결과를 배열로 반환 | 변형 |
```js
const fruits = ['apple', 'banana', 'coconut']

// pop
console.log(fruits.pop()) // coconut
console.log(fruits) // ['apple', 'banana']

// push
fruits.push('orange')
console.log(fruits) // ['apple', 'banana', 'orange']

// shift
console.log(fruits.shift()) // apple
console.log(fruits) // ['banana', 'orange']

// unshift
fruits.unshift('melon')
console.log(fruits) // ['melon', 'banana', 'orange']
```

## pop
* 배열 끝 요소를 제거하고, 제거한 요소를 반환
## push
* 배열 끝에 요소를 추가
## shift
* 배열 앞 요소를 제거하고, 제거한 요소를 반환
## unshift
* 배열 앞에 요소를 추가
## forEach
* 인자로 주어진 함수(콜백 함수)를 배열 요소 각각에 대해 실행
* 반환 값: **undefined**
* forEach 구조
  ```js
  array.forEach(function (item, index, array) {
    // do something
  })
  ```
* 콜백함수는 3가지 매개변수로 구성
    1. item: 배열의 요소
    2. index: 배열 요소의 인덱스
    3. array: 배열
* forEach 예시
  ```js
  const fruits = ['apple', 'banana', 'coconut']

  fruits.forEach(function (item, index, array) {
    console.log(`${item} / ${index} / ${array}`)
  })

  fruits.forEach((item, index, array) => {
    console.log(`${item} / ${index} / ${array}`)
  })
  ```

## map
* 배열 요소 전체를 대상으로 함수(콜백 함수)를 호출하고, 함수 호출 결과를 모아 **새로운 배열을 반환**
* 기본적으로 forEach 구조와 같으며 forEach와 달리 **새로운 배열**을 반환함
* map 구조
  ```js
  const result = array.map(function (item, index, array) {
    // do something
  })
  ```
* map 예시
  ```js
  // 1
  const fruits = ['apple', 'banana', 'coconut']

  const result = fruits.map(function (fruit) {
    return fruit.length
  })

  const result2 = fruits.map((fruit) => {
    return fruit.length
  })

  console.log(result) // [5, 6, 7]


  // 2
  const numbers = [1, 2, 3]

  const doubleNumber = numbers.map((number) => {
    return number * 2
  })

  console.log(doubleNumber) // [2, 4, 6]
  ```

## 콜백 함수 (callback function)
* 다른 함수에 인자로 전달되는 함수
  * 외부 함수내에서 호출되어 일종의 루틴이나 특정 작업을 진행

## 배열 정리
<!--  -->
# 99. 참고
## 배열 순회 종합
## 콜백함수 구조를 사용하는 이유
### 함수의 재사용성
### 비동기적 처리