# 99. Fixtures
## 목차
1. 개요
2. 초기 데이터 제공하기
## 학습 목표
* Django fixtures를 작성하는 방법을 학습하여 초기 데이터를 작성하고, fixtures를 추출하고 로드하여 활용하는 방법을 익힐 수 있다.

# 1. 개요
## fixtures
* Django가 데이터베이스로 가져오는 방법을 알고 있는 데이터 모음
* Django가 직접 만들기 때문에 데이터베이스 구조에 맞추어 작성 되어있음
* **Django는 fixtures를 사용해 모델에 초기 데이터를 제공**

### 초기 데이터의 필요성
* 협업
* Django 프로젝트의 앱을 처음 설정할 때 동일하게 준비된 데이터로 데이터베이스를 미리 채우는 것이 필요한 순간이 있다.
* Django에서는 fixtures를 사용해 앱에 초기 데이터(initial data)를 제공할 수 있다.

# 2. 초기 데이터 제공하기
> 데이터 사전준비 해두기
## fixtures 명령어
* `dumpdata`: 생성(데이터 추출)
* `loaddata`: 로드(데이터 입력)

### dumpdata
* 데이터베이스의 모든 데이터를 출력
* 여러 모델을 하나의 json 파일로 만들 수 있음
```console
$ python manage.py dumpdata [app_name[.ModelName] app_name[.ModelName] ...] > filename.json
```
```console
$ python manage.py dumpdata --indent 4 articles.article > article.json
$ python manage.py dumpdata --indent 4 articles.comment > comment.json
$ python manage.py dumpdata --indent 4 accounts.user > user.json
```
* ROOT에 json 파일 생성됨

### loaddata
* fixtures 기본 경로
  * `app_name/fixtures/`
* Django는 설치된 모든 app의 디렉토리에서 fixtures 폴더 이후의 경로로 fixtures 파일을 찾아 load 함
* fixtures 불러오기
    1. 해당 위치로 fixture 파일 이동
    ```
    articles/
      fixtures/
        articles.json
        comments.json
        user.json
    ```
    2. db.sqlite3 파일 삭제 후 migrate 진행
    3. load 후 데이터가 잘 입력되었는지 확인하기
    ```console
    $ python manage.py loaddata articles.json users.json comments.json
    ```
## loaddata 순서 주의사항
* loaddata를 한번에 실행하지 않고, 하나씩 실행한다면 모델 관계에 따라 순서가 중요할 수 있음
  * comment는 article에 대한 key 및 user에 대한 key가 필요
  * article은 user에 대한 key가 필요
* 즉, 현재 모델 관계에서는 user -> article -> comment 순으로 data를 넣어야 오류가 발생하지 않음
  ```console
  $ python manage.py loaddata users.json
  $ python manage.py loaddata articles.json
  $ python manage.py loaddata comments.json
  ```

# 99. 참고
## loaddata 시 encoding codec 관련 에러가 발생하는 경우
* *(한글 데이터가 있을 때)*
* 2가지 방법 중 택 1
    1. dumpdata 시 추가 옵션 작성
    ```console
    $ python -Xutf8 manage.py dumpdata ...[생략]
    ```
    2. 메모장 활용
        1. 메모장으로 json 파일 열기
        2. "다른 이름으로 저장" 클릭
        3. 인코딩을 UTF8로 선택 후 저장
### fixture는 직접 만드는 것이 아니다.
* **반드시 dumpdata를 사용하여 생성하는 것**

### ~~모든 모델을 한번에 dump 하기~~
* 권하지 않는 방법
```console
# 3개의 모델을 하나의 json 파일로
$ python manage.py dumpdata --indent 4 articles.article articles.comment accounts.user > data.json

# 모든 모델을 하나의 json 파일로
$ python manage.py dumpdata --indent 4 > data.json
```