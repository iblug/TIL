# 4963 섬의 개수 https://www.acmicpc.net/problem/4963
import sys
sys.stdin = open('4963_input.txt', 'r')



import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x,y):
    graph[x][y] = 2
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w:
            if graph[nx][ny] == 1:
                graph[nx][ny] = 2
                dfs(nx, ny)

# 상하좌우 좌상 좌하 우하 우상
dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for x in range(h):
        for y in range(w):
            if graph[x][y] == 1:
                dfs(x, y)
                cnt += 1
    print(cnt)
'''


import sys
input = sys.stdin.readline

def dfs(x,y):
    stack = [(x, y)]
    graph[x][y] = 2
    while stack:
        x, y = stack.pop()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == 1:
                    stack.append((nx, ny))
                    graph[nx][ny] = 2

# 상하좌우 좌상 좌하 우하 우상
dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for x in range(h):
        for y in range(w):
            if graph[x][y] == 1:
                dfs(x, y)
                cnt += 1
    print(cnt)
'''