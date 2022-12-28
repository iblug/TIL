# Git Hub

## 학습 목표
GitHub 원격저장소에 로컬 저장소를 올려 관리할 수 있다.  
원격저장소 활용 명령어를 이해하고 설명할 수 있다.

## 개요

> **원격 저장소에 버전(커밋)를 관리한다!**
* [github](https://github.com/)

- [깃허브리포트](https://octoverse.github.com/)

## 명령어
* remote
  * 원격저장소 설정을 처음 할 때
  * 로컬저장소를 원격저장소에 처을 올릴 때
  * 원격 저장소의 정보를 확인
```
$ git remote add origin <URL>
$ git remote -v
```

- push
  - 로컬 저장소의 버전(커밋)을 원격저장소로 보낼 때
```
$ git push origin master
```

* pull
  * 원격저장소의 버전(커밋)을 로컬 저장소로 가져올 때
```
$ git pull origin master
```
- clone
  - 원격 저장소에 있는 프로젝트를 복제하여 모든 버전을 로컬 저장소에 가져올 때
```
$ git clone <url>
```

## push 실패
- 협업을 하다보면 아래의 오류 메시지를 확인하게됨
![push_conflict](image/push_conflict.png)
* 로컬 저장소와 원격저장소의 커밋 이력이 다른 경우 push할 때 오류 발생
* 해결 방법
 1. 원격 저장소의 커밋을 로컬 저장소로 가져옴(pull)
 2. 로컬에서 두 커밋을 병합(추가 커밋 발생)
    * 동시에 같은 파일이 수정된 경우 merge conflict가 발생
 3. 다시 GitHub으로 push

## gitignore
* 프로젝트에서 버전 관리를 별도로 하지 않는 파일/폴더가 발생
* git 저장소에 .gitignore 파일을 생성하고 해당 내용을 관리한다.
* 작성 예시
  * 특정 파일 : test/a.txt
  * 특정 폴더 : /secret
  * 특정 확장자 : *.exl
  * 예외 처리 : !b.exl
* *이미 커밋된 파일은 반드시 삭제를 하여야 .gitignore로 적용*
  * *따라서 프로젝트 시작전이나 파일을 커밋하기전에 미리 설정*

### 주로 어떤 파일을 gitignore
- [개발 언어](https://github.com/github/gitignore)
    - 예시) 파이썬: venv/, 자바스크립트: node_modules/
- 개발 환경
    - 운영체제 (windows, mac, linux)
    - 텍스트 에디터 / IDE (visual studio code 등)
- [gitignore.io](https://gitignore.io) - .gitignore 파일 만든는 사이트 
