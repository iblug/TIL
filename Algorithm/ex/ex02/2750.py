# https://www.acmicpc.net/problem/2750
# 수 정렬하기

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
s = [int(input) for _ in range(N)]
# s = []
# for _ in range(N):
#     s.append(int(input()))

s.sort()
for i in s:
    print(i)