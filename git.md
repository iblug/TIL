# Git/Git Hub
## 정의
* Git은 분산버전관리스스템으로 코드의 버전을 관리하는 도구  
* 2005년 리눅스 커널을 위한 도구로 리누스 토르발스가 개발  
* 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율
## 환경 설정
* 사용자 정보(commit author) : 커밋을 하기 위해 반드시 필요
  * git config --global user.name "username"
    * Github에서 설정한 username으로 설정
  * git config --global user.email "my@email.com"
    * Github에서 설정한 email로 설정
* 설정 확인
  * git config -l
  * git config --global -l
  * git config user.name

* --system
  * /etc/gitconfig
  * 시스템의 모든 사용자와 모든 저장소에 적용(관리자 권한)
* --global
  * ~/.gitconfig
  * 현재 사용자에게 적용되는 설정
* --local
  * .git/config
  * 특정 저장소에만 적용되는 설정



## 명령어
