# 2739 구구단 https://www.acmicpc.net/problem/2739
import sys
sys.stdin = open('2739_input.txt', 'r')

n = int(input())
for i in range(1, 10):
    print(f'{n} * {i} = {n*i}')