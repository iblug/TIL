# 스택(Stack)
## 스택 구현 예제 (Python)
* 선입후출(Last In First Out)
  * *ex) 박스, 프링글스통*
* `append` & `pop`
  * *C++ : push & pop, top*
  * *Java : push & pop, peek*
```py
stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
# [5, 2, 3, 1]
print(stack[::-1]) # 최상단 원소부터 출력
# [1, 3, 2, 5]
```

# 큐(Queue)
* 선입선출(First In First Out)
  * *ex) 터널, 대기열*
* `append` & `popleft`
  * *C++ : push & pop, front*
  * *Java : offer & poll*
* list로 구현하면 시간복잡도가 올라감
  * *list에서는 pop이후에 원소의 위치를 조정함*
* `from collections import deque`
```py
from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
# deque([3, 7, 1, 4])
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 순서대로 출력
# deque([4, 1, 7, 3])
```