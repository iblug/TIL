"""
1. 아래 할 일 생성
content : 실습 제출
priority : 5
completed : False
deadline : 오늘 날짜(년-월-일)
"""

todo = Todo()
todo.content = '실습 제출'
todo.priority = 5
todo.completed = False
deadline = '2023-03-28'
todo.save()

"""
2. 아래 할 일 생성
content : 데일리 설문(오후) 제출
deadline : 오늘 날짜(년-월-일)
"""
todo = Todo()
todo = Todo(content='데일리 설문(오후) 제출', deadline='2023-03-28')
todo.save()

"""
3. 임의의 할 일 5개 생성
"""
Todo.objects.create(content='복습하기')
# <Todo: Todo object (3)>

Todo.objects.create(content='알고리즘 문제풀기', deadline='2023-03-28')
# <Todo: Todo object (4)>

Todo.objects.create(content='실습 다시 해보기', priority=3)
# <Todo: Todo object (5)>

Todo.objects.create(content='TIL 작성', deadline='2023-03-28',priority=1)
# <Todo: Todo object (6)>

Todo.objects.create(content='운동', priority=5, completed=False)
# <Todo: Todo object (7)>

"""
4. pk 기준 오름차순으로 정렬한 모든 데이터 조회
"""

Todo.objects.order_by('pk')
# <QuerySet [<Todo: Todo object (1)>, <Todo: Todo object (2)>, <Todo: Todo object (3)>, <Todo: Todo object (4)>, <Todo: Todo object (5)>, <Todo: Todo object (6)>, <Todo: Todo object (7)>]>

"""
5. priority 기준 내림차순으로 정렬한 모든 데이터 조회
"""

Todo.objects.order_by('-priority')
# <QuerySet [<Todo: Todo object (1)>, <Todo: Todo object (7)>, <Todo: Todo object (2)>, <Todo: Todo object (3)>, <Todo: Todo object (4)>, <Todo: Todo object (5)>, <Todo: Todo object (6)>]>

"""
6. pk가 1인 단일 데이터의 아래 필드 조회
(pk, content, priority, deadline, created_at)
"""

todo = Todo.objects.get(pk=1)
todo.pk
# 1
todo.content
# '실습 제출'
todo.priority
# 5
todo.deadline
todo.created_at
# datetime.date(2023, 3, 28)