# 서버의 이해
## 1. IP와 도메인
* IP(Internet Protocol)
  * IP 주소(IP Address)는 네트워크에 연결된 모든 컴퓨터가 가지고 있는 숫자로 이루어진 고유 주소(ex. 123.456.789.101)
* 도메인
  * 도메인 이름(Domain Name)는 문자로 이루어진 IP 주소
  * 일반 사용자는 IP 주소보다는 도메인 이름을 사용하기 때문에 중간 계층에서 이를 변환하는 DNS(Domain Name System)을 사용한다.

* 참고
  * [인터넷은 어떻게 동작하는가?](https://developer.mozilla.org/ko/docs/Learn/Common_questions/Web_mechanics/How_does_the_Internet_work)

## 2. 클라이언트와 서버
![img](https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/How_the_Web_works/client-server.jpg)

* 클라이언트
  * 일반적인 웹 사용자의 **인터넷이 연결된 장치들**과 이런 장치들에서 이용가능한 **웹에 접근하는 소프트웨어**(일반적으로 Chrome)
  * 서비스를 요청하는 주체
* 서버
  * 웹페이지, 사이트, 또는 앱을 저장하는 컴퓨터
  * 클라이언트의 요청에 응답하는 주체
- 참고
  * [웹의 동작 방식](https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
  * [웹 서버란 무엇일까?](https://developer.mozilla.org/ko/docs/Learn/Common_questions/Web_mechanics/What_is_a_web_server)

## 3. 정적 웹 사이트와 동적 웹 사이트의 차이점
* 정적 웹 사이트 (Static sites)
  * 특별한 리소스 요청이 들어올 때 서버에서 하드 코딩된 **동일한 콘텐츠**를 반환
* 동적 웹 사이트 (Dynamic sites)
  * 필요할 때에 **동적으로 응답 콘텐츠가 생성**
  * 보통 HTML 템플릿에 있는 자리 표시자에 **데이터베이스에서 가져온 데이터를 넣어 생성**
  * 사용자또는 저장된 환경을 기반으로 URL에 대해 **다른 데이터를 반환** 할 수 있음
  * **응답을 반환하는 과정에서 다른 작업을 수행** 할 수 있음(ex. 알림 보내기)
  
### 3-1. Django는 무엇을 위한 도구인가?
* framwork
  * 일반적인 문제를 해결하고 **개발 속도를 높임**
  * 특정 도메인에서 직면하는 **다양한 유형의 작업을 단순화**하도록 설계된 함수, 객체, 규칙 및 기타 코드 구성 요소의 모음
  * **클라이언트** 측 웹 프레임 워크는 **레이아웃 및 프리젠테이션 작업을 단순화**
  * **서버** 측 웹 프레임 워크는 직접 구현해야하는 많은 **"공통"웹 서버 기능**을 제공
- 참고
  * [Introduction to the server side](https://developer.mozilla.org/ko/docs/Learn/Server-side/First_steps/Introduction)

## 4. HTTP와 요청/응답 메시지
* HTTP (HyperText Transfer Protocol)
  * HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜
  * 웹 서버와 사용자의 인터넷 브라우저 사이에 문서를 전송하기 위해 사용되는 통신 규약

* 요청 메시지

  ![](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview/http_request.png)

  * HTTP Method
    * `GET`: 리소스를 가져옴
    * `POST`: HTML form의 데이터를 전송
    * 그 외 다른 동작이 요구될 수도 있음
  * Path(경로)
    * 프로토콜, 도메인, TCP 포트
  * Version of the protocol(HTTP 프로토콜의 버전)
  * Headers
    * 추가 정보를 전달하는 선택적 헤더들

* 응답 메시지

  ![](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview/http_response.png)

  * HTTP 프로토콜의 버전
  * Status code
    * 요청의 성공 여부와 그 이유를 나타내는 상태 코드
    * [Status code](https://developer.mozilla.org/ko/docs/Web/HTTP/Status)
  * Status message
    * 상태 코드의 짧은 설명을 나타내는 상태 메시지
  * Headers

* 참고
  * [HTTP 개요](https://developer.mozilla.org/ko/docs/Web/HTTP/Overview)

## 5. Server-side web frameworks
* 서버측 웹 프레임워크
  *  작성하기 쉽고, 웹 어플리케이션을 유지및 보수하기 쉽게 만드는 소프트웨어 프레임워크
* 무엇을 제공하는가?
  * URL 라우팅 핸들러
  * 데이테베이스와 상호작용
  * 유저 인증과 세션 지원
  * 출력 형식 설정(예: HTML, JSON, XML)
  * 웹 공격에 대처하기 위한 보안 강화 같은 일반적인 웹 개발 작업을 단순화하는 도구와 라이브러리를 제공
- 참고
  * [Server-side web frameworks](https://developer.mozilla.org/ko/docs/Learn/Server-side/First_steps/Web_frameworks)

# 99. 추천 영상
[[ youtube ] CS50 2017-Lecture6-HTTP](https://www.youtube.com/watch?v%3DPUPDGbnpSjw)