# https://www.acmicpc.net/problem/2480
# 주사위 세개

import sys
sys.stdin = open('input.txt', 'r')

a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
elif (a == b) or (a == c): # b != c
    print(1000 + a * 100)
elif b == c: # a != b
    print(1000 + b * 100)
else: # a != b != c
    print(max(a, b, c) * 100)
