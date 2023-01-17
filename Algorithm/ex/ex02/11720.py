# https://www.acmicpc.net/problem/11720
# 숫자의 합

import sys
sys.stdin = open('input.txt', 'r')

_ = int(input())
print(sum(map(int, input())))