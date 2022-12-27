# 마크다운

## 개요

마크다운(Markdown)은 2004년 존 그루버가 만든 텍스트 기반의 마크업 언어(HTML, CSS)다.

## 특징

마크다운은 최소한의 문법으로 구성되어 있으며 순수 텍스트로 작성 가능하다.

다른 환경에서 변환하여 보여진다.

## 예시

'README.md'나 정적사이트생성기 기반 블로그 등에서 활용한다.

---
---

# 마크다운 문법 정리

수업내용과 [여기](https://www.markdownguide.org/cheat-sheet/)를 참고하여 작성하였습니다.

더 많은 내용은 [여기](https://namu.wiki/w/%EB%82%98%EB%AC%B4%EC%9C%84%ED%82%A4%3A%EB%AC%B8%EB%B2%95%20%EB%8F%84%EC%9B%80%EB%A7%90)를 확인.

---

## 텍스트 강조

*기울리기* \*기울리기\*  
**강조** \*\*강조\*\*  
`code` \`code\`  
~~취소선~~ \~~취소선\~~
>인용구 > 인용구

---

## 리스트

```md
1. First item
  - item
  - item
2. Second item

* Third item
  1. First item
  2. Second item
  3. Third item
* item
```

1. First item
  - item
  - item
2. Second item

* items
  1. First item
  2. Second item
  3. Third item
* item
---

## 링크
```md
[구글](https://google.com)  
![이미지](image.png)
[a 파일](a.md)
[b 폴더](b/)
```
[구글](https://google.com/)  
![이미지](image.png)  
[a 파일](a.md)  
[b 폴더](b/)

---

## 테이블

> [테이블 쉽게 만들기](https://www.tablesgenerator.com/markdown_tables)

```md
| wow | 1  | 2  | 3   | 4   |
|-----|----|----|-----|-----|
| a   | a1 | a2 | a3  | a4  |
| b   | b1 | b2 | b3  | b4  |
| c   | 1  | 22 | 333 | 444 |
```

| wow | 1  | 2  | 3   | 4   |
|-----|----|----|-----|-----|
| a   | a1 | a2 | a3  | a4  |
| b   | b1 | b2 | b3  | b4  |
| c   | 1  | 22 | 333 | 444 |

---

## 코드블럭

```python
print('Hello, World')
# 주석입니다.
```

\```python  
print('Hello, World')  
\# 주석입니다.  
\```

---
---

## 개발자에게 문서 작성이란..?

- 자신이 경험한 사용법을 문서화해서 팀 내에 전파

- 기술 문서 작성 및 관리 업무