# https://www.acmicpc.net/problem/11721
# 열 개씩 끊어 출력하기

import sys
sys.stdin = open('input.txt', 'r')

s = input()
for i in range(0, len(s), 10):
    print(s[i:i+10])