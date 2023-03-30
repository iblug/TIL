from django.shortcuts import render, redirect
from .models import Article


# Create your views here.
def index(request):
    # DB에 전체 게시글 조회를 요청하고 쿼리셋을 응답받아 저장
    articles = Article.objects.all()
    # print(articles)
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article =Article.objects.get(pk=pk)
    # print(article)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    # new에서 보낸 사용자 데이터를 받음
    # print(request.GET)
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 받은 데이터를 DB에 저장
    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2
    article = Article(title=title, content=content)
    # 저장 전에 유효성 검사
    article.save()

    # 3
    # Article.objects.create(title=title, content=content)

    # 결과 페이지 반환
    # return render(request, 'articles/create.html')
    # return index(request) # 잘못된 방법

    # 이동 주소(URL)를 사용자에게 응답
    # return redirect('articles:index')

    # 생성한 글의 단일 조회(DETAIL) 주소(URL)로 이동 응답
    return redirect('articles:detail', article.pk)


def delete(request, pk):
    article = Article.objects.get(pk=pk)

    # 조회한 데이터 삭제(DELETE)
    article.delete()

    # 전체 조회 페이지 이동
    return redirect('articles:index')


def edit(request, pk):
    # 수정할 데이터 조회
    article = Article.objects.get(pk=pk)

    context = {
        'article': article
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    # 수정 작업 과정
    # 1. 데이터 조회 -> delete
    article = Article.objects.get(pk=pk)

    # 2. 데이터 수정
    # 2-1. 사용자가 입력한 form 데이터 할당 -> create
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 2-2. 조회한 데이터(article)의 필드 값 변경
    article.title = title
    article.content = content

    # 3. 데이터 저장 -> create
    article.save()

    return redirect('articles:detail', pk)
    