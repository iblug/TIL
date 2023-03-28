# ORM
## 목차
1. 개요
2. QuerySet API
3. ORM CREATE
4. ORM READ
## 학습 목표
* django ORM을 사용해 QuerySet이란 무엇인지 이해하고, 데이터베이스에서 데이터를 가져오는 방법을 습득한다.
* QuerySet에서 데이터를 필터링하는 다양한 방법들을 학습하고, 적절한 방법을 선택할 수 있는 API를 학습한다.

# 1. 개요
## ORM
* Object Relational Mapping
* 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 프로그래밍 기술

# 2. QuerySet API
* ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화하는데 사용하는 도구
  * (API를 사용하여 SQL이 아닌 Python 코드로 데이터를 처리)
* querySet API 구문
 * `Article.objects.all()`
 * Model class . manager . Queryset API
## Query
* 데이터베이스에 특정한 데이터를 보여달라는 요청
* "쿼리문을 작성한다."
  * -> 원하는 데이터를 얻기위해 데이터베이스에 요청을 보낼 코드를 작성한다.
* 이 때, 파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 QuerySet이라는 자료 형태로 변환하여 우리에게 전달

## QuerySet
* 데이터베이스에게서 전달 받은 객체 목록(데이터 모음)
  * 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음
* Django ORM을 통해 만들어진 자료형
* 단, 데이터베이스가 단일한 객체를 반환할 때는 QuerySet이 아닌 모델(Class)의 인스턴스로 반환됨

# 3. ORM CREATE
## QuerySet API 실습 사전 준비
* 외부 라이브러리 설치 및 설정
```console
$ pip install ipython
$ pip install django-extensions
```
```py
# settings.py

INSTALLED_APPS = [
  'articles',
  'django_extensions',
  ...,
]
```
```console
$ pip freeze > requirements.txt
```

## Django shell
* django 환경 안에서 실행되는 python shell
  * (입력하는 QuerySet API 구문이 django 프로젝트에 영향을 미침)

## 데이터 객체를 만드는(생성하는) 3가지 방법
### 1. 첫번째 방법(인스턴스 변수 하나씩)
```shell
# 특정 테이블에 새로운 행을 추가하여 데이터 추가

>>> article = Article() # Aricle(class)로 부터 article(instance)

>>> article.title = 'first' # 인스턴스 변수 (title)에 값을 할당
>>> article.content = 'django' # 인스턴스 변수 (content)에 값을 할당

# save를 하지 않으면 아직 DB에 값이 저장되지 않음

>>> article
<Article: Article object (None)>

>>> Article.objects.all()
<QuerySet []>

# save를 하고 확인하면 저장된 것을 확인할 수 있다.

>>> article.save()
>>> article
<Article: Article object (1)>
>>> article.id
1
>>> article.pk
1
>>> Article.objects.all()
<QuerySet [Article: Article object (1)]>

# 인스턴스인 article을 활용하여 변수에 접근해보자(데이터 저장된 것을 확인)
>>> article.title
'first'
>>> article.content
'django!'
>>> article.created_at
datetime.datetime(2023, 1, 1, 2, 43, 56, 49345, tzinfo=<UTC>)
```

### 2. 두번째 방법(인스턴스 바로 초기화)
```shell
>>> article = Article(title='second', content='django')

# 아직 저장 되어있지 않음
>>> article
<Article: Article object (None)>

# save를 호출해야 저장됨
>>> article.save()
>>> article
<Article: Article object (2)>
>>> Article.objects.all()
<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]>
```

### 3. 세번째 방법(바로 생성)
```shell
# 위 2가지 방식과는 다르게 바로 생성된 데이터가 반환된다.

>>> Article.objects.create(title='third', content='django')
<Article: Article object (3)>
```
## save()
* 객체를 데이터베이스에 저장하는 메서드

# 4. ORM READ
## 전체 데이터 조회
* all()
  ```shell
   >>> Article.objects.all()
  <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>

  ```
  * return new QuerySets
    * 객체 목록(list)을 반환함
    
## 단일 데이터 조회
* get()
  ```shell
  >>> Article.objects.get(pk=1)
  <Article: Article object (1)>

  # 없을 때
  >>> Article.objects.get(pk=100)
  DoseNotExist: Article matching query does not exist.
  
  # 다수를 찾을 때
  >>> Article.objects.get(content='django!')
  MultipleObjectReturned: get() returned more than one Article -- it return 2!
  ```
  * 객체를 찾을 수 없으면 DoseNotExist 예외를 발생시키고,  \
  둘 이상의 객체를 찾으면 MultipleObjectReturned 예외를 발생시킴
  * **primary key**와 같이 고유성(uniqueness)을 보장하는 조회에서 사용해야 함
  * do not return QuerySets

## 특정 조건 데이터 조회
* return new QuerySets
* filter()
  ```shell
  >>> Article.objects.filter(content='django')
  <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>

  # 없으면 비어있는 QuerySet 반환
  >>> Article.objects.filter()
  <QuerySet []>

  # 단일 QuerySet
  >>> Article.objects.filter(title='first')
  <QuerySet [<Article: Article object (1)>]>
  ```

# 99. 참고
## QuerySet API 관련 문서
* [QuerySet API reference](https://docs.djangoproject.com/en/3.2/ref/models/querysets/)
* [Making queries](https://docs.djangoproject.com/en/3.2/topics/db/queries/#limiting-querysets)
* [장고걸스 튜토리얼](https://tutorial.djangogirls.org/ko/django_orm/)

## Field lookups
* 특정 레코드에 대한 조건을 설정하는 방법
* QuerySet 메서드 filter().exclude() 및 get()에 대한 키워드 인자로 지정됨
  * [Field lookups](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#field-lookups)
  ```console
  # Field lookups 예시

  # "content 컬럼에 'dj'가 포함된 모든 데이터 조회"
  >>> Article.objects.filter(content__contains='dj')
  ```

## query문 보기
* .query
  ```console
  >>> print(Article.objects.all().query)
  ```

## ORM, QuerySet API를 사용하는 이유
* 데이터베이스 쿼리를 추상화하여 Django 개발자가 데이터베이스와 직접 상호작용하지 않아도 되도록 함
* 데이터베이스와의 결합도를 낮추고 개발자가 더욱 직관적이고 생산적으로 개발할 수 있도록 도움