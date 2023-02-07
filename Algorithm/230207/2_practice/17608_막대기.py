# 17608 막대기 https://www.acmicpc.net/problem/17608
import sys
sys.stdin = open('17608_input.txt', 'r')

import sys, heapq
input = sys.stdin.readline

n = int(input())

h = [int(input())]
for _ in range(n-1):
    a = int(input())
    while h and h[0] <= a:
        heapq.heappop(h)
    heapq.heappush(h, a)

print(len(h))    







#