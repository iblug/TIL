from django.shortcuts import render, redirect
from .models import Todo

# 할 일 전체 조회 index
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)

# 할 일 단일 조회 detail
def detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo': todo,
    }
    return render(request, 'todos/detail.html', context)

# 할 일 생성 new
def new(request):
    return render(request, 'todos/new.html')

# 할 일 생성 create
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    priority = request.POST.get('priority')
    deadline = request.POST.get('deadline')
    
    if deadline:
        todo = Todo(title=title, content=content, priority=priority, deadline=deadline)
    else:
        todo = Todo(title=title, content=content, priority=priority)

    # if not deadline:
    #     deadline = None

    # todo = Todo(title=title, content=content, priority=priority, deadline=deadline)

    todo.save()

    return redirect('todos:detail', todo.pk)

# 할 일 삭제 delete
def delete(request):
    temp = request.POST.get('pk')
    todo = Todo.objects.get(pk=temp)
    todo.delete()
    return redirect('todos:index')

# 할 일 수정 edit
def edit(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo': todo,
    }
    return render(request, 'todos/edit.html', context)

# 할 일 수정 update
def update(request, pk):
    todo = Todo.objects.get(pk=pk)

    title = request.POST.get('title')
    content = request.POST.get('content')
    priority = request.POST.get('priority')
    deadline = request.POST.get('deadline')

    todo.title = title
    todo.content = content
    todo.priority = priority
    
    if deadline:
        todo.deadline = deadline
    else:
        todo.deadline = None

    todo.save()

    return redirect('todos:detail', pk)

# 완료 여부
def done(request, pk):
    todo = Todo.objects.get(pk=pk)

    if todo.completed:
        todo.completed = False
    else:
        todo.completed = True

    todo.save()
    
    return redirect('todos:index')