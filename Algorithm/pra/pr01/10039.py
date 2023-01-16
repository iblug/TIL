# https://www.acmicpc.net/problem/10039
# 평균점수

import sys
sys.stdin = open('input.txt', 'r')

sum = 0
for _ in range(5):
    num = int(input())
    sum += num if num > 40 else 40
print(sum//5)