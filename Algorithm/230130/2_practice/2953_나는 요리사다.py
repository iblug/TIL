# 2953 나는 요리사다 https://www.acmicpc.net/problem/2953
import sys
sys.stdin = open('2953_input.txt', 'r')

n = s = 0
for i in range(5):
    s_ = sum(list(map(int, input().split())))
    if s_ > s:
        s = s_
        n = i+1
print(n, s)