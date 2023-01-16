# https://www.acmicpc.net/problem/10886
# 0 = not cute / 1 = cute

import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
s = ''
for _ in range(n):
    s += input().split()
# print(s)
# print(s.count('0'))
if s.count('0') > len(s) // 2:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')