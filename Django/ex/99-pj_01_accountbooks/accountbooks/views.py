from django.shortcuts import render, redirect
from .models import AccountBook
from django.db.models import Sum

# 가계부 전체 조회 index
def index(request):
    abs = AccountBook.objects.all()
    
    choice = request.GET.get('choice',' ')
    abs = choice_category(abs, choice)
    
    date_from = request.GET.get('date_from', '')
    date_to = request.GET.get('date_to', '')
    abs = date_range(abs, date_from, date_to)

    sort = request.GET.get('sort', ' ')
    abs = sort_accounts(abs, sort)

    sum_ = abs.aggregate(Sum('amount'))
    
    context = {
        'abs': abs,
        'choice': choice,
        'date_from': date_from,
        'date_to': date_to,
        'sort': sort,
        'sum': sum_['amount__sum'],
    }
    # print(context['date_from'])
    return render(request, 'abs/index.html', context)

# 분류
def choice_category(queryset, choice):
    if choice == '식비':
        return queryset.filter(category='식비')
    elif choice == '카페':
        return queryset.filter(category='카페')
    elif choice == '교통비':
        return queryset.filter(category='교통비')
    elif choice == '문화생활':
        return queryset.filter(category='문화생활')
    elif choice == '의류':
        return queryset.filter(category='의류')
    else:
        return queryset

# 정렬
def sort_accounts(queryset, sort):
    if sort == 'amount':
        return queryset.order_by('amount')
    elif sort == 'amount_desc':
        return queryset.order_by('-amount')
    elif sort == 'date':
        return queryset.order_by('date')
    elif sort == 'date_desc':
        return queryset.order_by('-date')
    elif sort == 'pk':
        return queryset.order_by('pk')
    elif sort == 'pk_desc':
        return queryset.order_by('-pk')
    else:
        return queryset
    
# 기간
def date_range(queryset, date_from, date_to):
    if date_from and date_to:
        return queryset.filter(date__range=(date_from, date_to))
    elif date_from:
        return queryset.filter(date__gte=date_from)
    elif date_to:
        return queryset.filter(date__lte=date_to)
    else:
        return queryset

# 가계부 단일 조회 detail
def detail(request, account_book_pk):
    ab = AccountBook.objects.get(pk=account_book_pk)
    context = {
        'ab': ab,
    }
    return render(request, 'abs/detail.html', context)

# 가계부 생성 new
def new(request):
    return render(request, 'abs/new.html')

# 가계부 생성 create
def create(request):
    note = request.POST.get('note')
    category = request.POST.get('category')
    amount = request.POST.get('amount')
    date = request.POST.get('date')
    description = request.POST.get('description')

    ab = AccountBook(note=note, category=category, amount=amount, date=date, description=description)

    ab.save()

    return redirect('abs:detail', ab.pk)

# 가계부 수정 edit
def edit(request, account_book_pk):
    ab = AccountBook.objects.get(pk=account_book_pk)
    context = {
        'ab': ab,
    }

    return render(request, 'abs/edit.html', context)

# 가계부 수정 update
def update(request, account_book_pk):
    ab = AccountBook.objects.get(pk=account_book_pk)

    ab.note = request.POST.get('note')
    ab.category = request.POST.get('category')
    ab.amount = request.POST.get('amount')
    ab.date = request.POST.get('date')
    ab.description = request.POST.get('description')

    ab.save()

    return redirect('abs:detail', ab.pk)

# 가계부 삭제 delete
def delete(request, account_book_pk):
    ab = AccountBook.objects.get(pk=account_book_pk)
    
    ab.delete()

    return redirect('abs:index')

# 가계부 복사 copy
def copy(reqeust, account_book_pk):
    ab = AccountBook.objects.get(pk=account_book_pk)
    ab2 = AccountBook(note=ab.note, description=ab.description, category=ab.category, amount=ab.amount, date=ab.date)
    ab2.save()

    return redirect('abs:index')