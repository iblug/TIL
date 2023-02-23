# Web-Fundaemtals of HTML and CSS
## 목차
1. Introduction of web page
2. Structuring the web
    1. Introduction ot HTML
    2. Structure of HTML
    3. Text Structure
3. Styling the web
    1. Introduction to CSS
    2. Select elements
    3. Cascade & Specificity
## 학습 목표
* HTML 문서의 구조를 이해하고, 태그를 사용하여 웹 페이지의 구조와 콘텐츠를 작성할 수 있다.
* CSS 속성과 값의 구조를 이해하고, 스타일 시트를 사용하여 웹 페이지의 디자인과 레이아웃을 구성할 수 있다.
* CSS 선택자를 이해하고, 스타일을 적용할 요소를 선택하는 방법을 익힐 수 있다.

# 1. Introduction of web page
* World Wide Web
  * 인터넷으로 연결된 컴퓨터들이 정보를 공유하는 거대한 정보 공간
* Web site
  * 인터넷에서 여러 개의 Web page가 모인 것으로, 사용자들에게 정보나 서비스를 제공하는 공간
* Web page
  * HTML, CSS, JavaScript 들의 웹 기술을 이용하여 만들어진, 하나의 인터넷 문서
    * *Structure, Styling, Behaviour*
  
# 2. Structuring the web
## 2-1. Introduction to HTML
* HTML
  * Hyper Text Markup Langage
  * 웹 페이지의 의미와 구조를 정의하는 언어
* Hypertext
  * 웹 페이지를 다른 페이지로 연결하는 링크
  * 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
* Markup Language
  * 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
    * HTML, Markdown

## 2-1. Structure of HTML
### HTML Element
```html
<p>My cat is very grumpy</p>
```
* 하나의 요소는 여는 태그와 닫는 태그 그리고 그 안의 내용으로 구성됨
* 닫는 태그는 태그 이름 앞에 슬래시가 포함되며 닫는 태그가 없는 태그도 존재

### HTML Attrivutes
```html
<p class="editor-note">My cat is very grumpy</p>
```
* 규칙
  * 요소 이름 다음에 바로 오는 속성은 요소 이름과 속성 사이에 공백이 있어야 함
  * 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분함
  * 속성 값은 열고 닫는 따옴표로 감싸야 함
* 목적
  * 나타내고 싶지 않지만 추가적인 기능, 내용을 담고 싶을 때 사용
  * CSS가 해당 요소를 선택하기 위한 값으로 활용됨

### HTML 문서의 구조
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>My page</title>
  </head>
  <body>
    <p>This is my page</p>
  </body>
</html>
```
* `<!DOCTYPE html>`
  * 해당 문서가 html로 문서라는 것을 나타냄
* `<html>` `</html>`
  * 전체 페이지의 콘텐츠를 포함
* `<title>` `</title>`
  * 브라우저 탭 및 즐겨찾기 시 표시되는 제목으로 사용
* `<head>` `</head>`
  * HTML 문서에 관련된 설명, 설정 등
  * 사용자에게 보이지 않음
* `<body>` `</body>`
  * 페이지에 표시되는 모든 콘텐츠

## 2-3. Text Structure
* HTML Text Structure
  * HTML의 주요 목적 중 하나는 텍스트 구조와 의미를 제공하는 것
    * 예를 들어 `<h1>`은 단순히 텍스트를 크게 만드는 것이 아닌 해당 **문서의 최상위 제목**이라는 의미를 부여하는 것
* 대표적인 HTML Text structure
  * Heading & Paragraphs: **h1~6, p**
  * Lists: **ol, ul, li**
    * Unordered
    * Ordered
  * Emphasis & Importance: **em, strong**
* ex)
```html
<body>
  <h1>Main Heading</h1>
  <h2>Sub Heading</h2>
  <p>This is my page</p>
  <p>This is <em>emphasis</em></p>
  <p>Hi <strong>my name</strong> is Air</p>
  <ol>
    <li>파이썬</li>
    <li>알고리즘</li>
    <li>디비</li>
  </ol>
</body>
```
