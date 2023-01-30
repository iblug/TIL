# 2438 별 찍기 - 1 https://www.acmicpc.net/problem/2438
import sys
sys.stdin = open('2438_input.txt', 'r')

for i in range(1, int(input())+1):
    print('*'*i)
# [print('*' * (i + 1)) for i in range(int(input()))]