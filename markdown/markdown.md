# 마크다운(Markdown)
## 목차
0. [개요](#개요)
1. [특징](#특징)
2. [마크다운 문법](#마크다운-문법)
3. [off the record](#off-the-record)
## 개요
![Markdown](../image/Markdown.png)

마크다운은 2004년 존 그루버가 만든 텍스트 기반의 마크업 언어(HTML, CSS)다.

## 특징

* 장점
  * 문법이 간단해 읽고 쓰는 것이 쉬워서 글을 빠르게 작성할 수 있다.
  * 다양한 형태로 변환이 가능하고 지원하는 프로그램과 플랫폼이 다양하다.
    * 'README.md'나 정적사이트생성기 기반 블로그 등에서 활용한다.

- 단점
  - 표준이 없어서 도구에 따라서 변환방식이나 생성물이 다르다.

<br>

---
<br>

# 마크다운 문법
1. [텍스트 강조](#텍스트-강조)
2. [공백과 줄바꿈](#공백과-줄바꿈)
3. [리스트](#리스트ol-ul)
4. [링크](#링크)
5. [문단](#문단-제목)
6. [테이블](#테이블)
7. [코드블럭](#코드블럭)

## 텍스트 강조

| 출력 | 입력 |
|:---:|:---:|
| *기울리기* | \*기울리기\* |
| **강조** | \*\*강조\*\* |
| `code` | \`code\` |
| ~~취소~~ | \~~취소\~~ |
>인용구 &nbsp; &nbsp; &nbsp; &nbsp; > 인용구

---
## 공백과 줄바꿈

* 공백

```md
&nbsp;
```

* 줄바꿈

```md
<br>
```

---

## 리스트(ol, ul)

```md
# md

1. First item
    1. item
    2. item
2. Second item
    * item

* items
  1. First item
  2. Second item
* item
  - item
    - item
```

1. First item
    1. item
    2. item
2. Second item
    * item

* items
  1. First item
  2. Second item
* item
  - item
    - item
---

## 링크
```md
# md

[구글](https://google.com)  
[README 파일](../README.md)
[git 폴더](../git/)
![이미지](../image/image1.png) 

```
[구글](https://google.com/)  
[README 파일](../README.md)  
[git 폴더](../git/)  
![이미지](../image/image1.png)  

---

## 문단 제목
```md
# md

# H1
## H2
### H3
#### H4
##### H5
```
# # H1
## H2
### H3
#### H4
##### H5

---

## 테이블


```md
# md

| 왼쪽 정렬 | 중앙 정렬 | 오른쪽 정렬 |
|:---------|:---------:|----------:|
|   내용1   |   내용2   |   내용3   |
|   내용4   |   내용5   |   내용6   |
```

| 왼쪽 정렬 | 중앙 정렬 | 오른쪽 정렬 |
|:---------|:---------:|----------:|
|   내용1   |   내용2   |   내용3   |
|   내용4   |   내용5   |   내용6   |

> [테이블 쉽게 만들기](https://www.tablesgenerator.com/markdown_tables)

---

## 코드블럭

```md
# md

```python  
print('Hello, World')  
# 주석입니다.  
\``` 
```

```python
print('Hello, World')
# 주석입니다.
```




---

수업내용과 [여기](https://www.markdownguide.org/cheat-sheet/), [여기](https://kimasill.tistory.com/entry/MarkDown-%EB%A7%88%ED%81%AC%EB%8B%A4%EC%9A%B4-%EB%AC%B8%EC%84%9C-%EC%9E%91%EC%84%B1%EB%B2%95)를 참고하여 작성하였습니다.

더 많은 내용은 [나무위키](https://namu.wiki/w/%EB%82%98%EB%AC%B4%EC%9C%84%ED%82%A4%3A%EB%AC%B8%EB%B2%95%20%EB%8F%84%EC%9B%80%EB%A7%90)를 확인.

---
---
## off the record

### 개발자에게 문서 작성이란..?

- 자신이 경험한 사용법을 문서화해서 팀 내에 전파 할 수있어야 한다.[링크](https://d2.naver.com/news/3435170)
- '테크니컬 라이팅(Technical Writing)'[링크](https://developers.google.com/tech-writing)
- 기술 문서 작성 및 관리 업무 [링크](https://engineering.linecorp.com/ko/blog/write-the-docs-prague-2018-recap/)

> ## 🏠 [go to README](../README.md)