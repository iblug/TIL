# https://www.acmicpc.net/problem/9085
# 더하기

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for _ in range(T):
    _ = int(input()) # input() 
    print(sum(list(map(int, input().split()))))