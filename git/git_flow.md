# Git Flow
![git_flow](../image/git_flow.png)
> Git을 활용한 협업의 흐름

# 목차
1. [Branch](#1-branch)
2. [merge](#2-merge)
3. [GitHub flow 기본원칙](#3-github-flow-기본-원칙)
4. [GitHub flow models](#4-github-flow-models)

# 1. Branch
**독립적인 작업흐름을 만들고 관리**하기 위하여 사용한다.


* 브랜치 생성
  ```
  (master) $ git brach {branch name}
  ```
  
* 브랜치 이동
  ```
  (master) $ git checkout {branch name}
  ```
  
* 브랜치 생성 및 이동
  ```
  (master) $ git checkout -b {branch name}
  ```
  
* 브랜치 목록
  ```
  (master) $ git brach
  ```
  
* 브랜치 삭제
  ```
  (master) $ git brach -d {branch name}
  ```

[🔝](#git-flow)

# 2. merge

* 각 branch에서 작업을 한 이후 이력을 합치기 위해 사용한다.
```
(master) $ git merge feature
```

* branch 병합 시나리오
  1. fast-foward
      * 기존 master 브랜치에 변경사항이 없을 경우.
      * 단순히 앞으로 이동한다
  2. merge commit
      * 서로 다른 파일이 수정된 경우.
      * 병합 커밋 발생한다.
  3. merge conflict
      * 서로 같은 파일이 수정된 경우.
      * 충돌 메세지가 뜬다.
      * 해당 파일의 위치에 표준형식에 따라 표시해준다.
      * 원하는 형태의 코드로 직접 수정을 하고 직접 커밋을 한다.

- 병합 후 필요에 따라 barnch 삭제한다.

[🔝](#git-flow)

# 3. GitHub Flow 기본 원칙
1. master branch는 반드시 **배포 가능한 상태**여야 한다.
2. feature branch는 **각 기능의 의도를 알 수 있도록 작성**한다.
3. Commit message는 매우 중요하며, **명확하게** 작성한다.
4. Pull Request를 통해 협업을 진행한다.
5. 변경사항을 반영하고 싶다면, **master** branch에 병합한다.

# 4. GitHub flow models

## 1. Shared Repository Model

* Push에 직접적인 권한이 **있다.**
* 동일한 저장소를 공유하여 활용한다.
  1. 팀원을 초대하고 저장소를 Clone.
  2. branch에서 작업 및 GitHub Push.
  3. Pull Request(PR) 생성.
  4. Review 및 Merge.

## 2. Fork & Pull Model
* Push에 직접적인 권한이 **없다.**
  1. Fork & Clone.
     * *Clone시 반드시 본인 저장소인지 확인할 것*
  2. branch에서 작업 및 GitHub Push.
  3. Pull Request(PR) 생성.
  4. branch는 삭제하고, master branch를 업데이트.
      * *단, master branch는 원본 저장소를 받아와야 하며 별도의 원격 저장소를 추가하여 진행할 수 있다.*
      * *혹은 GitHub에서 fetch upstream도 가능하다.

[🔝](#git-flow)
> ## [🏠HOME](../README.md)