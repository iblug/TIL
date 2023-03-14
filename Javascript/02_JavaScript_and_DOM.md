# JavaScript and DOM
## 목차
1. JavaScript 개요
2. DOM 기본 개념
3. DOM Query(선택)
4. DOM Manipulation(조작)
## 학습 목표
* 웹 브라우저에서의 JavaScript의 역할을 정의할 수 있다.
* 웹 페이제의 HTML과 CSS를 JavaScript에서 다룰 수 있는 DOM에 대해 이해하고, 웹 페이지의 요소들을 조작할 수 있다.
* DOM 조작에 사용되는 메소드와 속성을 적절히 사용할 수 있다
# 1. JavaScript 개요
* JavaScript 실행 환경
  1. HTML script 태그
  2. js 확장자 파일
  3. 브라우저 console

# 2. DOM 기본 개념
## DOM(Document Object Model)
* 웹 페이지(Document)를 구조화된 객체로 제공하며 **프로그래밍 언어가 웹 페이지를 사용할 수 있게** 연결시킴
## 브라우저가 웹 페이지를 불러오는 과정
* 문서(Document)는 웹 브라우저를 통해 해석되어 화면에 나타남
* DOM은 이러한 문서를 조작하는 방법을 제공하는 API
* 브라우저는 HTML 문서를 해석하여 **DOM tree**라는 객체의 트리로 구조화 함
* DOM에서 모든 요소, 속성, 텍스트는 하나의 객체이며 모두 document 객체의 자식
* 웹 페이지를 동적으로 만드는 것 == 웹 페이지를 **조작**(생성, 추가, 삭제)하는 것
* 조작하기 위한 순서
  1. 조작 하고자 하는 요소를 **선택**또는 **탐색**
  2. 선택된 요소의 콘텐츠 또는 속성 **조작**
## 'document'object
* 웹 페이지 객체
* DOM Tree의 진입점
* 페이지를 구성하는 모든 객체 요소를 포함

# 3. DOM Query (선택)
* 요소 하나 선택: ducument.querySelector()
* 요소 여러 개 선택: document.querySelectorAll()
```js
console.log(document.querySelector('.title'))
console.log(document.querySelector('.text'))

console.log(document.querySelectorAll('.text'))

console.log(document.querySelectorAll('ul > li'))
```
## 선택 메서드 정리
* document.querySelector(selector)
  * 제공한 선택자와 일치하는 element 한 개 선택
  * 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환 (없다면 null 반환)
* document.querySelectorAll(selector)
  * 제공한 선택자와 일치하는 여러 emement를 선택
  * 매칭할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
  * 제공한 CSS selector를 만족하는 NodeList를 반환

# 4. DOM Manipulation (조작)
## 조작 목차
1. 속성(attribute) 조작
    * 클래스 속성 조작
    * 일반 속성 조작
2. HTML 콘텐츠 조작
3. DOM 조작
4. style 조작
### 클래스 속성 조작
* 'class' property
  * 요소의 클래스 목록을 DOMTokenList(유사 배열) 형태로 반환
  * add()와 remove() 메서드를 사용해 지정한 클래스 값을 추가 혹은 제거
  * element.classList.add()
    * 지정한 클래스 값을 추가
  * element.classList.remove()
    * 지정한 클래스 값을 제거
### 일반 속성 조작
* 조회: .getAttribute()
* 설정(수정): .setAttribute()
* 삭제: .removeAttribute()
### HTML 콘텐츠 조작
* 'textContent' property
  * 요소의 텍스트 콘텐츠를 표현
### DOM 요소 조작
* 생성: .createElement()
* 추가: .appendChild()
* 삭제: .removeChild()
### style 조작
* 'style' property
  * 해당 요소의 모든 스타일 속성 목록을 포함하는 속성

# 99. 참고
## 요소별 DOM property 확인 Tip
* 개발자도구 - Elements - Properties에서 해당 요소의 모든 DOM property 확인 가능
## .appendChild()
* 이미 문서에 존재하는 요소를 다른 요소의 자식으로 삽입하는 경우 위치를 이동
## Parsing(파싱)
* 구문 분석, 해석
* 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정
  * Parsing > Style > Layout