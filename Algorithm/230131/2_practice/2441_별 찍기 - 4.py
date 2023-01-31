# 2441 별 찍기 - 4 https://www.acmicpc.net/problem/2441
import sys
sys.stdin = open('2441_input.txt', 'r')

n = int(input())
[print(('*'*i).rjust(n)) for i in range(n, 0, -1)]