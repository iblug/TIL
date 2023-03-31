from django.shortcuts import render, redirect
from .models import AccountBook
from django.db.models import Sum

# Create your views here.
def index(request):
    abs = AccountBook.objects.all()
    choice = request.GET.get('choice',' ')
    abs = choice_category(abs, choice)
    sort = request.GET.get('sort', ' ')
    abs = sort_accounts(abs, sort)
    sum_ = abs.aggregate(Sum('amount'))
    context = {
        'abs': abs,
        'choice': choice,
        'sort': sort,
        'sum': sum_['amount__sum'],
    }
    return render(request, 'abs/index.html', context)


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
    

def detail(request, account_book_pk):
    ab = AccountBook.objects.get(pk=account_book_pk)
    context = {
        'ab': ab,
    }
    return render(request, 'abs/detail.html', context)


def new(request):
    return render(request, 'abs/new.html')


def create(request):
    note = request.POST.get('note')
    category = request.POST.get('category')
    amount = request.POST.get('amount')
    date = request.POST.get('date')
    description = request.POST.get('description')

    ab = AccountBook(note=note, category=category, amount=amount, date=date, description=description)

    ab.save()

    return redirect('abs:detail', ab.pk)


def edit(request, account_book_pk):
    ab = AccountBook.objects.get(pk=account_book_pk)
    context = {
        'ab': ab,
    }

    return render(request, 'abs/edit.html', context)


def update(request, account_book_pk):
    ab = AccountBook.objects.get(pk=account_book_pk)

    ab.note = request.POST.get('note')
    ab.category = request.POST.get('category')
    ab.amount = request.POST.get('amount')
    ab.date = request.POST.get('date')
    ab.description = request.POST.get('description')

    ab.save()

    return redirect('abs:detail', ab.pk)

def delete(request, account_book_pk):
    ab = AccountBook.objects.get(pk=account_book_pk)
    
    ab.delete()

    return redirect('abs:index')


def copy(reqeust, account_book_pk):
    ab = AccountBook.objects.get(pk=account_book_pk)
    ab2 = AccountBook(note=ab.note, description=ab.description, category=ab.category, amount=ab.amount, date=ab.date)
    ab2.save()

    return redirect('abs:index')