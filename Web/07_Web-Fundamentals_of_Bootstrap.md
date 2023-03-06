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

