# 문제풀이
## 음료수 얼려먹기 
* 5-10 149

|입력|출력|
|-|-|
|5 4<br>00110<br>00011<br>11111<br>00000|3|
|15 14<br>00000111100000<br>11111101111110<br>11011101101110<br>11011101100000<br>11011111111111<br>11011111111100<br>11000000011111<br>01111111111111<br>00000000011111<br>01111111111000<br>00011111111000<br>00000001111000<br>11111111110011<br>11100011111111<br>11100011111111<br>|8

* 내가 푼 답

```py
import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

def find_(x, y):
    graph[x][y] = '1'
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if graph[nx][ny] == '0':
                find_(nx, ny)
    return True


n, m = map(int, input().split())
graph = [list(map(str,input())) for _ in range(n)]
# print(graph)
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0 , 0, -1, 1]

count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '0':
            find_(i, j)
            count += 1
print(count)
```

* 예시 답
```py
# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result) # 정답 출력
```
## 미로 탈출 
* 5-11 152

|입력|출력|
|--|--|
3 3<br>110<br>010<br>011<br>|5
5 6<br>101010<br>111111<br>000001<br>111111<br>111111<br>|10


* 나의 답
    
```py
def find_(x, y, a, b):
    if x < 0 or y < 0 or x >= n or y >= m or graph[x][y] == 0:
        return False
    if visited[x][y] == False:
        graph[x][y] += graph[a][b]
        visited[x][y] = True
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            find_(nx, ny, x, y)
    return True

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

find_(0,0,0,0)
print(graph[n-1][m-1]-1)
```

* 예시 답
    * BFS, 큐를 사용하자
```py
from collections import deque

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))
```