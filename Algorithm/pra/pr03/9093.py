# https://www.acmicpc.net/problem/9093
# 단어 뒤집기

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for _ in range(T):
    s = sys.stdin.readline().split()
    for i in s:
        print(i[::-1], end=' ')
    print()