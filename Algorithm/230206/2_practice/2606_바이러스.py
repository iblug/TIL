# 2606 바이러스 https://www.acmicpc.net/problem/2606
import sys
sys.stdin = open('2606_input.txt', 'r')

"""
import sys
input = sys.stdin.readline

def dfs(x):
    visited[x] = 1
    for i in graph[x]:
        if not visited[i]:
            visited[i] = 1
            dfs(i)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(1)
print(sum(visited)-1)
""" 



import sys
input = sys.stdin.readline

def dfs(x):
    stack = [x]
    visited[x] = 1
    while stack:
        cur = stack.pop()
        for i in graph[cur]:
            if not visited[i]:
                stack.append(i)
                visited[i] = 1

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(1)
print(sum(visited)-1)