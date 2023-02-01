# 1436 영화 감독 숌 https://www.acmicpc.net/problem/1436
import sys
sys.stdin = open('1436_input.txt', 'r')

n = int(input())

cnt = 0
i = 0
while cnt < n:
    i += 1
    if '666' in str(i):
        cnt += 1
    
print(i)