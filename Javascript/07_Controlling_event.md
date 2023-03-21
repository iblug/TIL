# Controlling Event
## 목차
## 학습목표

# 1. 개요
* 일상속의 이벤트
  * 버튼을 눌러서 도어락을 열거나, 전화기의 버튼을 눌러서 통화를 시작하는 것
  * 키모드를 사용하여 글을 쓰거나, 리모컨을 사용하여 채널을 변경하는 것
  * 알람 시계를 설정하여 특정 시간에 알림을 받는 것
* 웹에서의 이벤트
  * 버튼을 클릭했을 때 모달이 출력되는 것
  * 마우스 커서의 위치에 따라 드래그 앤 드롭하는 것
  * 사용자가 입력한 값에 따라 새로운 요소를 생성하는 것
* 일상생활에서의 이벤트처럼 웹에서도 이벤트를 통해 특정 동작을 수행한다.

# 2. 이벤트
* 무언가 일어났다는 신호, 사건
  * (모든 DOM 요소는 이러한 신호를 만들어 냄)
* 종류
  * 마우스, 인풋, 키보드, 터치 등
* DOM 요소는 event를 받고 받은 event를 '처리'할 수 있음
  * 이벤트 핸들러(처리기)
## envent handler
* 이벤트가 발생했을 때 실행되는 함수
  * (사용자의 행동에 어떻게 반응할지를 JS코드로 표현한 것)
* .addEventListener()
  * 대표적인 이벤트 핸들러 중 하나
  * (특정 이벤트를 DOM 요소가 수신할 때 마다 콜백 함수를 호출)

  ```js
  EventTarget.addEventListener(type, handler)
  ```

  * EventTarget: DOM 요소
  * type: 특정 이벤트
  * handler: 콜백 함수
  * "대상에 특정 Event가 발생하면, 할 일을 등록한다."
* type
  * 이벤트 이름(ex.'click)
  * [이벤트 종류(mozilla)](https://developer.mozilla.org/en-US/docs/Web/Events)
* handler
  * 발생한 이벤트 객체를 수신하는 콜백 함수
  * 콜백 함수는 발생한 Event object를 유일한 매개변수로 받음
* 실습

# 3. 이벤트 핸들러 활용
## click 이벤트
## input 이벤트
## click & input 이벤트
## 이벤트 취소하기
* .preventDefault()
  * 현재 Event의 기본 동작을 중단
## todo
## 로또 번호 생성기

### lodash
* 모듈성, 성능 및 추가 기능을 제공하는 JavaScript 유틸리티 라이브러리
* array, object 등 자료구조를 다룰 때 사용하는 유용하고간편한 함수들을 제공
* [https://lodash.com/](https://lodash.com/)

# 99. 참고
## addEventListener와 this
* addEventListener에서의 콜백 함수는 특별하게 function 키워드의 경우 addEventListener를 호출한 대상을(event.target) 뜻함
## 참고 사이트
* [MDN addEventListener](https://developer.mozilla.org/ko/docs/Web/API/EventTarget/addEventListener)
* [MDN Event 유형](https://developer.mozilla.org/en-US/docs/Web/Events)
* [참고 블로그(이벤트 종류)](https://yoonjong-park.tistory.com/entry/addEventListener-%EC%9D%B4%EB%B2%A4%ED%8A%B8%EB%A6%AC%EC%8A%A4%EB%84%88-%EC%A2%85%EB%A5%98)
