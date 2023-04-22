from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
from django.http import JsonResponse
# Create your views here.

def index(request):
    posts = Post.objects.order_by('-pk')

    get_date_filter = request.GET.get('date_filter','')
    posts = filter_date(posts, get_date_filter)

    get_order = request.GET.get('order','')
    posts = sort_order(posts, get_order)

    context = {
        'posts': posts,
        'get_order': get_order,
    }
    return render(request, 'posts/index.html', context)


def filter_date(queryset, date_filter):
    if date_filter:
        date_filter = int(date_filter)
        return queryset.filter(created_at__gte=timezone.now()-timedelta(days=date_filter))
    else:
        return queryset


def sort_order(queryset, order):
    if order == 'voter':
        return queryset.alias(voter=(Count('select1_user')+Count('select2_user'))).order_by('-voter')
    elif order == 'likes':
        return queryset.alias(likes=Count('like_users')).order_by('-likes')
    elif order == 'newest':
        return queryset.order_by('-pk')
    elif order == 'old':
        return queryset.order_by('pk')
    else:
        return queryset


def detail(request, post_pk):
    # 역참조 및 m:n - prefetch_related
    # 정참조 - select_related

    # 게시글
    post = Post.objects.select_related('user').prefetch_related(
                                        'comment_set', 'select1_user',
                                        'select2_user', 'like_users').get(pk=post_pk)

    select1_user_count = post.select1_user.count()
    select2_user_count = post.select2_user.count()
    
    # 댓글
    comments = post.comment_set.select_related('user').prefetch_related('like_users').all()
    get_order = request.GET.get('order','')
    comments = sort_order(comments, get_order)
    
    comment_form = CommentForm()

    context = {
        'post': post,
        'select1_user_count':select1_user_count,
        'select2_user_count':select2_user_count,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'posts/detail.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # 저장 x, 인스턴스만 생성
            post = form.save(commit=False)
            post.user = request.user
            # 저장
            post.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)

@login_required
def select(request, post_pk, answer):
    post = Post.objects.get(pk=post_pk)
    user = request.user
    if user in post.select1_user.all() or user in post.select2_user.all():
        return redirect('posts:detail', post_pk=post_pk)

    if answer == post.select1_content:
        post.select1_user.add(user)
    elif answer == post.select2_content:
        post.select2_user.add(user)
    else:
        return redirect('posts:detail', post_pk=post_pk)

    return redirect('posts:detail', post_pk=post_pk)


@login_required
def comment_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.post = post
        comment.save()
    return redirect('posts:detail', post.pk)

#게시글 좋아요
@login_required
def likes(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if post.like_users.filter(pk=request.user.pk).exists():
        post.like_users.remove(request.user)
        is_liked = False
    else:
        post.like_users.add(request.user)
        is_liked = True
    
    # 게시글 좋아요 수
    post_like_count = post.like_users.count()
    
    context = {
          'is_liked': is_liked,
          'post_like_count': post_like_count,
    }
    return JsonResponse(context)


# 댓글 좋아요
@login_required
def comment_like(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    # 이미 좋아요 한 경우
    if comment.like_users.filter(pk=request.user.pk).exists():
        comment.like_users.remove(request.user)
    else:
        comment.like_users.add(request.user)
    return redirect('posts:detail', post_pk)

