# 완전 탐색(Exhaustive Search)
## 목차
1. 무식하게 풀기(Brute-force)
2. 델타 탐색(Delta Search)

# 1. 무식하게 다 해보기(Brute-force)
* **모든 경우의 수**를 탐색하여 문제를 해결하는 방식
  * 가장 단순한 풀이 기법이며, 단순 조건문과 반복문을 이용해서 풀 수 있음
  * 복잡한 알고리즘 보다는, 아이디어를 어떻게 코드로 구현할 것인지가 중요

* [BOJ 2798 블랙잭](https://www.acmicpc.net/problem/2798)
  * 특별한 알고리즘 기법 없이, 모든 경우의 수를 탐색

# 2. 델타 탐색(Delta Search)
* **이차원 리스트의 완전탐색**에서 많이 등장하는 유형인 **델타 탐색(상하좌우 탐색)**
* (0, 0)(특별한 지점)에서 부터 이차원 리스트의 모든 원소를 순회하며(완전탐색) **각 지점에서 상하좌우에 위치한 다른 지점을 조회하거나 이동**하는 방식
* **델타(delta)값**
  * 행과 열의 변량(-1, +1, ...)

|(x-1,y-1)|(x-1,y)|(x-1,y+1)|
|:-:|:-:|:-:|
|(x,y-1)|(x,y)|(x,y+1)|
|(x+1,y-1)|(x+1,y)|(x+1,y+1)|

## 델타 탐색 구현
```py
# 1) 델타값 정의(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 2)이차원 리스트 순회
for x in range(n):
    for y in range(m):

    # 3) 델타값을 이용해 상하좌우 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dx[i]

        # 4) 범위를 벗어나지 않으면 갱신
        if 0 <= nx < n and 0 <= ny < m:
          x = nx
          y = ny
```
## 8방 탐색
```py
# 상, 하, 좌, 우, 좌상, 좌하, 우상, 우하
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]
```