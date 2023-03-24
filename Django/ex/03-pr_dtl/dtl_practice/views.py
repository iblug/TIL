from django.shortcuts import render
import random

foods = ['치킨', '삼겹살', '짜장면']
# Create your views here.

def index(request):
    return render(request, 'index.html')

def today_dinner(request):
    global foods
    food = random.sample(foods, 1)
    context = {
        'food': food
    }
    return render(request, 'today_dinner.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    data = request.GET.get('content')
    context = {
        'data': data
    }
    return render(request, 'catch.html', context)

def lotto_create(request):

    return render(request, 'lotto_create.html')

def lotto(request):
    nums = range(1, 46)
    count = request.GET.get('count')
    sixnums = []
    for _ in range(int(count)):
        sixnum = sorted(random.sample(nums, 6))
        sixnums.append(sixnum)
    
    context = {
        'sixnums': sixnums,
    }
    
    return render(request, 'lotto.html', context)