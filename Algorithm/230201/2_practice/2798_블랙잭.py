# 2798 블랙잭 https://www.acmicpc.net/problem/2798
import sys
sys.stdin = open('2798_input.txt', 'r')

# n, m = map(int, input().split())
# c = list(map(int, input().split()))

# max_value = []
# for i in range(n-2):
#     for j in range(i+1, n-1):
#         for k in range(j+1, n):
#             now = c[i] + c[j] + c[k]
#             if now <= m:
#                 max_value.append(now)
# print(max(max_value))

from itertools import combinations

n,m=map(int, input().split())
s=list(map(int, input().split()))

d=list(combinations(s, 3))

max_value = []
for i in d:
    now = sum(i)
    if m >= now:
        max_value.append(now)
print(max(max_value))