# https://www.acmicpc.net/problem/2576
# 홀수
""" 
data = [int(input()) for _ in range(7)]
result = [a for a in data if a % 2 == 1]
result.sort()
if result:
    print(sum(result))
    print(result[0])
else:
    print(-1)
"""
import sys
sys.stdin = open('input.txt', 'r')

data = [a for a in map(int, sys.stdin.readlines()) if a % 2 == 1]
if data:
    print(sum(data))
    print(min(data))
else:
    print(-1)