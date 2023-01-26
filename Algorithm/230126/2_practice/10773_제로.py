# 10773 제로 https://www.acmicpc.net/problem/10773

import sys
input = sys.stdin.readline

k = int(input())
stack = []
for _ in range(k):
    n = int(input())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)
print(sum(stack))