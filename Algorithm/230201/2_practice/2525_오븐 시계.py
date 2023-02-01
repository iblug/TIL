# 2525 오븐 시계 https://www.acmicpc.net/problem/2525
import sys
sys.stdin = open('2525_input.txt', 'r')

a, b = map(int,input().split())
c = int(input())
a += (b + c) // 60
print(a%24, (b+c)%60)