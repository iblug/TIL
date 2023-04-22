from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
from .forms import CustomUserChangeForm, CustomUserCreationForm, CustomUserAuthenticationForm, CustomUserPasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import JsonResponse

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('posts:index')
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(request ,request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:index')
    else:
        form = CustomUserAuthenticationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/login.html', context)

@login_required
def logout(request):
    if request.user.is_authenticated:
       auth_logout(request)
    return redirect('posts:index')

def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('posts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/signup.html', context)

@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('posts:index')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/update.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomUserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('posts:index')
    else:
        form = CustomUserPasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/change_password.html', context)


def profile(request, username):
    User = get_user_model()
    person = User.objects.prefetch_related('followings', 'followers', 'post_set','comment_set').get(username=username)

    comments = person.comment_set.select_related('post').all()
    
    context = {
        'person': person,
        'comments':comments,
    }
    return render(request, 'accounts/profile.html', context)


@login_required
def follow(request, user_pk):
    user = get_user_model()
    you = user.objects.get(pk=user_pk)
    me = request.user

    # 자기 자신 팔로우 x
    if you != me:
        # 이미 팔로우 중
        if me in you.followers.all():
            you.followers.remove(me)
            is_followd = False
        else:
            you.followers.add(me)
            is_followd = True
        context = {
            'is_followed'     : is_followd,
            'followings_count': you.followings.count(),
            'followers_count' : you.followers.count(),
        }
        return JsonResponse(context)
    return redirect('accounts:profile', you.username)