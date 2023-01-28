# 힙(Heap), 셋(Set)
## 목차
1. 힙(Heap)
2. 셋(Set)

# 1. 힙(Heap)
* 우선순위 큐(Priority Queue)
  * 순서가 아닌 우선순위를 기준으로 가져올 요소를 결정(dequeue)하는 큐
* 최댓값 또는 최솟값을 빠르게 찾아내도록 만들어진 데이터 구조
* 완전 이진 트리의 형태로 <u>느슨한 정렬 상태를 지속적으로 유지</u>
* 중복 값을 허용

| 연산 종류  | Enqueue  | Dequeue  | 최솟값 탐색  |
|:-:|:-:|:-:|:-:|
| 배열(Array)  | O(1)  | O(N)  | O(N)  |
| (정렬된 배열)  | O(N)  | O(1)  | O(1)  |
| 힙(Heap)  | O(logN)  | O(logN)  | O(1)  |

* 활용
  * 데이터가 **지속적으로 정렬**돼야 하는 경우
  * 데이터에 **삽입/삭제가 빈번**할 때
  
[힙 가시화](https://www.cs.usfca.edu/~galles/visualization/Heap.html)
* 파이썬의 heapq 모듈
  * Minheap(최소 힙)으로 구현되어 있음(가장 작은 값이 먼저옴)
  * 삽입, 삭제, 수정, 조회 **연산의 속도가 리스트보다 빠르다**

[공식문서](https://docs.python.org/ko/3/library/heapq.html?highlight%3Dheap#module-heapq)

[공식문서](https://docs.python.org/ko/3/tutorial/datastructures.html?highlight%3D%EB%A6%AC%EC%8A%A4%ED%8A%B8#using-lists-as-stacks)

| 연산 종류 | 힙(Heap) | 리스트(List) |
|:-:|:-:|:-:|
| Get Item | O(1) | O(1) |
| Insert Item | O(logN) | O(1) 또는 O(N) |
| Delete Item | O(logN) | O(1) 또는 O(N)|
| Search Item | O(N) | O(N) |

* `heapq.heapify()`, `heapq.heappop(heap)`, `heapq.heappush(heap,item)`

[BOJ 1927 최소힙](https://www.acmicpc.net/problem/1927)

[BOJ 11286 절댓값 힙](https://www.acmicpc.net/problem/11286)

# 2. 셋(Set)
* 수학에서의 '집합'을 나타내는 데이터 구조로 Python에서는 기본적으로 제공되는 데이터 구조
* 활용
  * 데이터의 **중복이 없어야 할 때**(고유값들로 이루어진 데이터가 필요할 때)
  * 정수가 아닌 데이터의 **삽입/삭제/탐색이 빈번히** 필요할 때
* 연산
  * `.add()`
  * `.remove()`
  * `|` (합)
  * `-` (차)
  * `&` (교)
  * `^` (대칭차)
* 셋(Set) 연산의 시간 복잡도

| 연산 종류 | 시간 복잡도 |
|---|---|
| 탐색 | O(1) |
| 제거 | O(1) |
| 합집합 | O(N) |
| 교집합 | O(N) |
| 차집합 | O(N) |
| 대칭 차집합 | O(N) |
  
[BOJ 14425 문자열 집합](https://www.acmicpc.net/problem/14425)

[BOJ 1269 대칭 차집합](https://www.acmicpc.net/problem/1269)