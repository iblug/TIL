# https://www.acmicpc.net/problem/10818
# 최소, 최대

import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N = input()
arr = list(map(int, input().split()))
print(min(arr), max(arr))