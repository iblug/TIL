# https://www.acmicpc.net/problem/10824
# 네 수

import sys
sys.stdin = open('input.txt', 'r')

a, b, c, d = input().split()
print(int(a + b)+int(c + d))