# Web - Fundamentals of Bootstrap
## 목차
1. 개요
2. Typography 및 Color
3. Component
## 학습 목표
* Bootstrap을 설치하고 기본 구성 요소, UI 요소 및 컴포넌트 사용방법에 대해 숙지할 수 있다.
* Bootstrap을 이용하여 웹 프로젝트를 구현하는 방법을 익히고, 실습에 적용할 수 있다.

# 1. 개요
## Bootstrap
* 프론트엔드 라이브러리(Toolkit)
  * 반응형 웹 디자인 & CSS 및 JS 기반의 컴포넌트와 스타일 제공
### 사용해 보기
1. Bootstrap 공식 문서
  * [https://getbootstrap.com/](https://getbootstrap.com/)
2. Docs - Quick start
3. 2번 "Include Bootstrap's CSS and JS" 코드 확인 및 가져오기
  * [https://getbootstrap.com/docs/5.3/getting-started/introduction/#quick-start](https://getbootstrap.com/docs/5.3/getting-started/introduction/#quick-start)
  * head와 body에 bootstrap CDN이 포함된 코드 블럭
```html
<head>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
</head>
<body>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
</body>
```
### Bootstrap 클래스명 맛보기
* [spacing](https://getbootstrap.com/docs/5.3/utilities/spacing/)
```html
<p class="mt-5">Hello, world!</p>
```
* mt-5
  * {property}{sides}-{size}
* boostrap에서 클래스 이름으로 Spacing을 표현하는 방법
* 이미 스타일이 작성되어 있고 독특한 규칙이 있는 클래스 이름까지
* 우리는 설명서를 보며 Bootstrap이라는 도구상자를 어떻게 사용할 지 학습할 것

# 2. Typography 및 Color
## Typograpy
* Headings
* Display headings
* Inline text elements
* List
## Bootstrap Color system
* Bootstrap이 지정하고 제공하는 색상 시스템
* Colors
* Text colors
* Background colors
* 실습
  * 너비와 높이가 각각 200px인 정사각형 작성

# 3. Component
* Bootstrap에서 제공하는 UI 관련 요소
  * 일관된 디자인, 쉬운 프로토타입 제작 및 사용자 경험
* 대표 Component 사용해보기
  * Alerts
  * Badges
  * Buttons
  * Cards
  * Navbar
  
# 99. 참고
## CND (Content Delivery Network)
* 지리적 제약 없이 빠르고 안전하게 콘텐츠를 전송할 수 있는 전송 기술
  * 서버와 사용자 사이의 물리적인 거리를 줄여 콘텐츠 로딩에 소요되는 시간을 최소화
  * (웹 페이지 로드 속도를 높임)
  * 지리적으로 사용자와 가까운 CDN 서버에 콘텐츠를 저장해서 사용자에게 전달
## Bootstrap CDN
1. Bootstrap 홈페이지 - Download - "Compiled CSS and JS" Download
2. CDN을 통해 가져오는 bootstrap css와 js 파일을 확인
3. bootstrap.css 파일을 참고하여, 현재까지 작성한 클래스에 적용된 스타일을 직접 확인
## Bootstrap을 사용하는 이유
* 손쉬운 반응형 웹 디자인 구현
* 빠른 개발과 유지보수
  * 미리 디자인된 다양한 컴포넌트 및 기능
  * 일관된 코드와 문서
* 커스터마이징(customizing)이 용이
* 크로스 브라우징(Cross browsing) 지원
  * 모든 주요 브라우저에서 작동하도록 설계되어 있음