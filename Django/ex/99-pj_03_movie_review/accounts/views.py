from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('reviews:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('reviews:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def signup(request):
    if request.user.is_authenticated:
        return redirect('reviews:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('reviews:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('reviews:index')

@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('reviews:index')

@login_required
def profile(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    
    if request.user != user:
        return redirect('reviews:index')
    
    reviews = user.review_set.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def profile_update(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    if request.user != user:
        return redirect('reviews:index')
    
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', user_pk)
    else:
        form = CustomUserChangeForm(instance=request.user)

    context = {
        'user': user,
        'form': form,
    }
    return render(request, 'accounts/update.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('accounts:profile', user.pk)
    
    form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)