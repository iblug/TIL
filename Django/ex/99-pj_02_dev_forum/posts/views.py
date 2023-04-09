from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from datetime import datetime

# Create your views here.


# index
def index(request):
    posts = Post.objects.all().order_by('-pk')
    today = datetime.now().strftime('%Y-%m-%d')
    select_sorting = request.GET.get('select_sorting')
    posts = sorting(posts, select_sorting)
    new_posts(posts)
    context = {
        'today': today,
        'posts': posts,
        'subject': '모든 글',
        'select_sorting': select_sorting,
    }
    return render(request, 'posts/index.html', context)

# 카테고리 filter
def category(request, subject):
    today = datetime.now().strftime('%Y-%m-%d')
    posts = Post.objects.all().filter(category=subject)
    posts2 = Post.objects.all().filter(notice=True)
    posts = posts.union(posts2).order_by('-pk')
    select_sorting = request.GET.get('select_sorting')
    posts = sorting(posts, select_sorting)

    new_posts(posts)

    context = {
        'today': today,
        'posts': posts,
        'subject': subject,
        'select_sorting': select_sorting,
    }
    return render(request, 'posts/index.html', context)

# 정렬
def sorting(queryset, select_sorting):
    if select_sorting == '최신순':
        return queryset.order_by('-pk')
    elif select_sorting == '오래된순':
        return queryset.order_by('pk')
    else:
        return queryset

# new_posts
def new_posts(posts):
    now = timezone.now()
    for post in posts:
        time_diff = now - post.created_at
        if time_diff < timezone.timedelta(hours=10):
            post.is_new = True
        else:
            post.is_new = False



# create
@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
        'subject': '글 작성',
    }

    return render(request, 'posts/create.html', context)

# 상세페이지
@login_required
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    context = {
        'post': post,
    }
    return render(request, 'posts/detail.html', context)

# 수정
@login_required
def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:detail', post_pk)
    else:
        form = PostForm(instance=post)
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'posts/update.html', context)

# 삭제
@login_required
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('posts:index')

