# https://www.acmicpc.net/problem/2562
# 최댓값

import sys
sys.stdin = open('input.txt', 'r')

arr = []
max_ = 0
for i in range(9):
    arr.append(int(input()))
    if arr[i] > max_:
        max_ = arr[i]
        result = i + 1
print(max_, result, sep='\n')