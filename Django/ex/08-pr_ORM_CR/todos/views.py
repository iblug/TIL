from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.

# 할 일 전체 조회 index
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todos/index.html', context)


# 할 일 단일 조회 detail
def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)


# 할 일 생성 new
def new(request):
    return render(request, 'todos/new.html')


# 할 일 생성 create
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    priority = request.GET.get('priority')
    deadline = request.GET.get('deadline')

    # if deadline == '':
    #     deadline = None

    if deadline:
        todo = Todo(title=title, content=content, priority=priority, deadline=deadline)
    else:
        todo = Todo(title=title, content=content, priority=priority)


    # todo = Todo(title=title, content=content, priority=priority, deadline=deadline)

    todo.save()
    
    return redirect('/todos/new/')
    # return render(request, 'todos/create.html')