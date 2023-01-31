# 9455 박스 https://www.acmicpc.net/problem/9455
import sys
sys.stdin = open('9455_input.txt', 'r')



import sys
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    m, n = map(int, input().split())
    d = [list(input().split()) for _ in range(m)]
    t = 0
    for i in range(n):
        c = 0
        for j in range(m):
            if d[j][i] == '1':
                c += 1
            elif d[j][i] == '0':
                if c > 0:
                    t += c
    print(t)
