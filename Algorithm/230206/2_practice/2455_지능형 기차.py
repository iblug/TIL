# 2455 지능형 기차 https://www.acmicpc.net/problem/2455
import sys
sys.stdin = open('2455_input.txt', 'r')

cnt = 0
p = []
for _ in range(4):
    a, b = map(int, input().split())
    cnt += -a+b
    p.append(cnt)
print(max(p))