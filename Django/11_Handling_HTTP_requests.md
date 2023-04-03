# Handling HTTP requests
## 목차
1. 개요
2. view 함수의 변화
## 학습 목표
* HTTP requests methods를 사용해 효율적인 view 함수 구조를 작성할 수 있다.

# 1. 개요
## HTTP requests 처리에 따른 view 함수 구조 변화
* new & create
  * 공통점
    * "데이터 생성 로직을 구현하기 위함"
  * 차이점
    * "new는 GET method 요청 처리"
    * "create는 POST method 요청 처리"

# 2. view 함수의 변화
## 2-1. create 로직
> `GET` articles/create/ <br/>
> `POST` articles/create/
## 2-1-1. new와 view 함수 결합
## 2-1-2. 새로운 create view 함수
```py
# articles/views.py

def create(request):
  if request.method == 'POST': # 1 # 2
    form = ArticleForm(request.POST)
    if form.is_valid():
      article = form.save()
      return redirect('articles:detail', article.pk)
  else:
    form = ArticleForm() # 3
  context = {
    'form': form,
  }
  return render(request, 'article/new.html', context)
```
1. request 객체의 method 값을 사용한 분기
2. POST 일 때는 과거 create 함수의 로직 처리
3. POST가 아닐 때는 과거 new 함수의 로직 처리
## 2-1-3. new url 정리
* 불필요해진 new url 제거 (urls.py)
## 2-1-4. 기존 new 관련 코드 수정
* index.html, create.html, new.html, views.create() 의 url 코드 수정

## 2-2. update 로직
> `GET` articles/update/ <br/>
> `POST` articles/update/
### 2-2-1. edit과 view 함수 결합
### 2-2-2. 새로운 update view 함수
```py
# article/views.py

def update(request, pk):
  article = Article.objects.get(pk=pk)
  if request.method == 'POST':
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
      form.save()
      return redirect('articles:detail', article.pk)
  else:
    form = ArticleForm(instance=article)
  context = {
    'article': article,
    'form': form,
  }
  return render(request, 'articles/update.html', context)
```
## 2-1-3. new url 정리
* 불필요해진 new url 제거 (urls.py)
## 2-1-4. 기존 new 관련 코드 수정
* index.html, update.html, edit.html, views.update() 의 url 코드 수정