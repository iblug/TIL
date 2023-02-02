# 1547 공 https://www.acmicpc.net/problem/1547
import sys
sys.stdin = open('1547_input.txt', 'r')

import sys
input = sys.stdin.readline

m = int(input())
k = '1'
for _ in range(m):
    a, b = input().split()
    if a == k:
        k = b
    elif b == k:
        k = a
print(k)