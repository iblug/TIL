# 스택(Stack)과 큐(Queue)
## 목차
0. 데이터 구조 & 알고리즘
1. 스택(Stack)
2. 큐(Queue)
3. 덱(Deque)
# 0. 데이터 구조 & 알고리즘
* 어떻게 **저장**하고  \
어떻게 **활용**(조작)할 수 있는지
# 1. 스택(Stack)
* Stack은 쌓는다는 의미로써, 마치 접시를 쌓고 빼듯이  \
**데이터를 한쪽에서만 넣고 빼는 자료구조**
* **LIFO(Last-in First-out, 후입선출)** 방식
  * *활용 : 히스토리, ctrl + z, 단어 뒤집기*
  * *알고리즘 : 괄호 매칭, 함수 호출(재귀 호출), 백트래킹, DFS(깊이 우선 탐색)*
* **push** : 스택에 새로운 데이터를 삽입하는 행위
  * `.append(<데이터>)`
* **pop** : 스택의 가장 마지막 데이터를 가져오는 행위
  * `.pop()`
- 파이썬은 **리스트(List)**로 스택을 간편하게 사용

* 기본 문제
  * [BOJ 10773. 제로](https://www.acmicpc.net/problem/10773)

# 2. 큐(Queue)
* **한 쪽 끝에서 데이터를 넣고, 다른 한 쪽에서만 데이터를 뺄 수 있는 자료구조**
* **FIFO(First-in First-out, 선입선출)** 방식
  * *활용 : 프로세스 관리(데이터 버퍼), 클라이언트/서버(Message Queue)*
  * *알고리즘 : BFS(너비 우선 탐색), 다익스트라 - 우선순위 큐
* **dequeue** : 큐의 맨 앞 데이터를 가져오는 행위
  * `.pop(0)`
* **enquue** : 큐의 맨 뒤에 데이터를 삽입하는 행위
  * `.append(<데이터>)`

- 큐 자료구조도 파이썬 **리스트(List)**로 스택을 간편하게 사용

* [BOJ 2161. 카드1](https://www.acmicpc.net/problem/2161)

# 3. 덱(Deque, Double-Ended Queue)
* **덱(Deque)** : **양 방향**으로 삽입과 삭제가 자유로운 큐
* **양 방향 삽입, 추출이 모두 큐 보다 훨씬 빠름**
  * *리스트를 이용한 큐 자료구조는 **데이터를 뺄 때** 큐 안에 있는 데이터가 많은 경우 **비효율적***
* `.appendleft(<데이터>)`, `.popleft()`, `.append(<데이터>)`, `.pop()`