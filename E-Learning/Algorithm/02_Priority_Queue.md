# 우선순위 큐(Priority Queue)
* 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
* **우선순위에 따라 처리하고 싶을 때**
* **최단 경로** 문제

## 우선순위 큐를 구현하는 방법
1. 단순히 리스트를 이용하여 구현한다.
2. 힙(heap)을 이용하여 구현한다.

* 데이터의 개수가 N개일 때
  |우선순위 큐 구현 방식|삽입 시간|삭제 시간|
  |--|--|--|
  |리스트|O(1)|O(N)|
  |힙(Heap)|O(logN)|O(logN)|
  * 단순히 N개의 데이터를 힙에 넣었다가 모두 꺼내는 작업은 정렬과 동일함 (힙 정렬)
    * 이 경우 시간 복잡도는 O(NlogN)

## 힙(Heap)의 특징

* **힙은 완전 이진 트리자료 구조**의 일종
* 힙에서는 항상 **루트 노드(root node)를 제거**
* heappush & heappop
  ```py
  import heapq
  h = []
  heapq.heappush(h, value)
  heapq.heappop(h)
  ```
* **최소 힙(min heap)**
  * 루트 노드가 가장 작은 값
  * 따라서 값이 가장 작은 데이터가 우선적으로 제거
* **최대 힙(max heap)**
  * 루트 노드가 가장 큰 값
  * 따라서 값이 큰 데이터가 우선적으로 제거
## 완전 이진 트리(Complete Binary Tree)
* 루트(root)노드부터 시작하여 왼쪽 자식 노드, 오른쪽 자식 노드 순서대로 데이터가 차례대로 삽입되는 트리(tree)를 의미

## 최소 힙 구성 함수: Min-Heapify()
* (상향식) 부모 노드로 거슬러 올라가며, 부모보다 자신의 값이 더 작은 경우에 위치를 교체
* 힙에 새로운 원소가 삽입되었을 때 O(logN)의 시간 복잡도로 힙 성질을 유지하도록 할 수 있음
* 힙에 원소가 제거되었을 때 O(logN)의 시간 복잡도로 힙 성질을 유지하도록 할 수 있음
    * 이후에 루트 노드에서부터 하향식으로(더 작은 자식 노드로) Heapify()를 진행

## 우선순위 큐 라이브러리를 활용한 힙 구현 예제 (Python)
* Python의 heapq library은 기본적으로 min heap
  * *Python에서 max heap 형태로 동작하는 형태가 필요하면  \
  데이터를 넣을때와 꺼낼때 마이너스(-)를 붙임*
  * *C++ : max heap*
  * *Java : min heap*
```py
import sys
import heapq
input = sys.stdin.readline

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)    # max heap : -value
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h)) # max heap : -heapq.heappop
    return result
    
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
res = heapsort(arr)
for i in range(n):
    print(res[i])
# 오름차순으로 출력
```