from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.


def index(request):
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    posts = Post.objects.all()
    context = {
        'today': today,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            # print(dir(post))
            # return redirect('posts:index')
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
    }

    return render(request, 'posts/create.html', context)

@login_required
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    context = {
        'post': post,
    }
    return render(request, 'posts/detail.html', context)


def category(request, subject):
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    posts = Post.objects.all().filter(category=subject).order_by('-pk')
    context = {
        'today': today,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

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

@login_required
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('posts:index')