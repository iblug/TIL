# https://www.acmicpc.net/problem/10952
# A + B - 5

import sys
sys.stdin = open('input.txt', 'r')

while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    print(a+b)

# while True:
#     r = sum(map(int, input().split()))
#     if r == 0:
#         break
#     print(r)