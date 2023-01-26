# 2720 세탁소 사장 동혁 https://www.acmicpc.net/problem/2720
import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
coins = [0] * 4
Q = 0.25
D = 0.1
N = 0.05
P = 0.01
coin = [Q, D, N, P]
t = int(input())
for _ in range(t):
    c = int(input())
    for i in range(4):
        coins[i] = int(c // (coin[i] * 100))
        c %= (coin[i] * 100)
    print(*coins)