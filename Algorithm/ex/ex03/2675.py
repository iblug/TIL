# https://www.acmicpc.net/problem/2675
# 문자열 반복

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for _ in range(T):
    a, b = input().split()
    for i in b:
        print(i*int(a), end='')
    print()