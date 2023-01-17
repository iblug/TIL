# https://www.acmicpc.net/problem/3009
# 네 점

import sys
sys.stdin = open('input.txt', 'r')


arr = [[],[]]
for _ in range(3):
    x, y = input().split()
    if x not in arr[0]:
        arr[0].append(x)
    else:
        arr[0].remove(x)
    if y not in arr[1]:
        arr[1].append(y)
    else:
        arr[1].remove(y)
print(*arr[0], *arr[1])

