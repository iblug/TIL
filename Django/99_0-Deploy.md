# django 웹 서비스 배포 - 클라우드타입 활용 
# 1. 환경 변수
1. 운영 체제(os) 단위에서 활용되는 변수
2. 시스템(os)상의 모든 프로세스(프로그램)에서 전역적으로 사용되는 변수
* 환경 변수 사용 목적
  1. 외부에 공개되면 안되는 값(django SECRET_KEY 등)의 노출을 막기 위해서
  2. 배포 환경에서 필요한 값을 할당하기 위해서
* [os]환경 변수 조회(터미널 입력)
  * Windows : `set`
  * mac : `printenv`
* [python]환경 변수 조회
  ```python
  import os

  print(os.environ) # 전체 환경 변수 조회
  print(os.getenv('환경변수 키')) # 특정 환경 변수 조회
  ```
## python-dotenv 활용 환경 변수 관리
  * python-dotenv?
    * `.env` 파일에서 key-value를 읽어 <u>**프로그램 환경 변수**</u>로 설정해주는 라이브러리
    * 중요한 데이터를 환경 변수 형태로 관리하여 외부에 노출되는 것을 막을 수 있음
### 사용법
1. 패키지 설치
```console
pip install python-dotenv
pip freeze > requirements.txt
```
2. manage.py와 동일한 경로에 `.env` 파일 생성
3. key-value 작성
  * [SECRET KEY 생성기](https://djecrety.ir/)(https://djecrety.ir/)
  ```py
  # .env
  
  SECRET_KEY = 'SECRET KEY 생성기를 통해 행성한 값'
  ```
4. SECRET_KEY 할당 코드 수정
```python
# settings.py

# 기존
SECRET_KEY = '기존 SECRET_KEY'

# ------------------------

# 수정
import os
form dotenv import load_dotenv

"""
load_dotenv()
.env 파일의 key-value를 프로그램 환경 변수에 등록
"""
load_dotenv()

"""
환경 변수에서 key가 SECRET_KEY인 value 불러오기
"""
SECRET_KEY = os.getenv('SECRET_KEY')
```
5. `.gitignore`에 `.env` 작성
  * 'gitignore.io'를 사용 하였다며 작성된 상태

# 2. 클라우드 타입 배포
* [클라우드 타입](https://app.cloudtype.io/)
  * PaaS(Platform as a Service) 형태의 클라우드 서비스로 Python Django 뿐만 아니라 여러 언어와 프레임워크의 서비스 배포를 지원
  * 현재 Early Access 단계로 Django 기준 2개의 서비스를 제한적 무료로 배포할 수 있음
## 초기 설정
> Github 로그인으로 진행
1. 클라우드타입 - Github 인증 확인

![django_99_0_01.png](img/deploy/django_99_0_01.png)
2. 계정 생성

![django_99_0_02.png](img/deploy/django_99_0_02.png)
3. 초기 설정

![django_99_0_03.png](img/deploy/django_99_0_03.png)

![django_99_0_04.png](img/deploy/django_99_0_04.png)

![django_99_0_05.png](img/deploy/django_99_0_05.png)

![django_99_0_06.png](img/deploy/django_99_0_06.png)

![django_99_0_07.png](img/deploy/django_99_0_07.png)

## 배포
> Github Django 프로젝트 저장소 준비
1. 클라우드 타입 프로젝트 생성

![django_99_0_08.png](img/deploy/django_99_0_08.png)

![django_99_0_09.png](img/deploy/django_99_0_09.png)

![django_99_0_10.png](img/deploy/django_99_0_10.png)

2. 설정 입력

![django_99_0_11.png](img/deploy/django_99_0_11.png)

![django_99_0_12.png](img/deploy/django_99_0_12.png)
```
SECRET_KEY : 이전에 생성한 SECRET KEY 입력
DJANGO_SUPERUSER_USERNAME : 관리자 아이디
DJANGO_SUPERUSER_EMAIL : 관리자 이메일
DJANGO_SUPERUSER_PASSWORD : 관리자 비밀번호
```

![django_99_0_13.png](img/deploy/django_99_0_13.png)
```shell
# Pre start Command 입력 커맨드
python manage.py migrate && python manage.py createsuperuser --noinput

# 명령어 설명
# python manage.py migrate : DB 마이그레이트
# python manage.py createsuperuser --noinput : 환경 변수를 활용하여 관리자 계정 생성
```
3. 배포

![django_99_0_14.png](img/deploy/django_99_0_14.png)
4. 빌드 완료 후 접속

![django_99_0_15.png](img/deploy/django_99_0_15.png)
5. `DisallowedHost` 오류 확인

![django_99_0_16.png](img/deploy/django_99_0_16.png)
6. `DisallowedHost` 오류 해결
```python
# settings.py

# 기존
ALLOWED_HOSTS = []

# 수정
ALLOWED_HOSTS = ['복사한 주소 붙여넣기']
```

* ALLOWED_HOSTS?

> django 프로젝트 서비스의 접속을 허용하는 호스트/도메인 문자열 목록

> HTTP Host header 공격을 방지하기 위함.

> 기본적으로 `localhost`, `127.0.0.1` 허용

7. git add commit push 후 재배포

![django_99_0_17.png](img/deploy/django_99_0_17.png)
### 터미널 명령어 입력 방법
> loaddata 등 명령어 입력이 필요할 때 터미널에서 명령어를 입력하는 방법
1. 터미널 진입

![django_99_0_18.png](img/deploy/django_99_0_18.png)
2. 터미널 실행

![django_99_0_19.png](img/deploy/django_99_0_19.png)
3. 명령어 입력
```shell
# 예시 (json 데이터가 있을때)

python manage.py loaddata xxx.json
```

# 99. 디버깅
## 개발 환경 테스트
> 특정 기능 오류 발생 시 개발환경에서 문제없이 작동하는지 확인
## 데이터 확인
> 데이터가 없는 상황에서 데이터가 필요한 기능을 수행한건지 확인
## django 에러 페이지 확인
> 에러 페이지(노란 화면)에서 에러 확인
## 503 에러
> 503 에러는 서버 자체가 실행되지 않은 경우

![django_99_0_20.png](img/deploy/django_99_0_20.png)
* 먼저 실행 로그부터 확인
  * 터미널 확인
  
  ![django_99_0_21.png](img/deploy/django_99_0_21.png)
  
  ![django_99_0_22.png](img/deploy/django_99_0_22.png)
1. `ModuleNotFoundError: No module named 'dotenv'`

![django_99_0_23.png](img/deploy/django_99_0_23.png)

  * 의존성 목록 `requirements.txt`을 생성안한 경우
  * 사용할 수 없는 패키지를 사용한 경우
  * 리눅스 환경에서 사용할 수 없는 패키지를 사용한 경우(pywin32 등)

2. `The SECRET_KEY setting must not be empty`

![django_99_0_24.png](img/deploy/django_99_0_24.png)

  * 클라우드타입 `SECRET_KEY` 환경 변수 수정안한 경우 또는 오타

![django_99_0_25.png](img/deploy/django_99_0_25.png)

  * 기타 환경변수 key-value 오타 확인
  