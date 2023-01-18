# https://www.acmicpc.net/problem/10988
# 팰린드롬인지 확인하기

import sys
sys.stdin = open('input.txt', 'r')
a = input()
print('01'[a==a[::-1]])