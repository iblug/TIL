# 2669 직사각형 네개의 합집합의 면적 구하기 https://www.acmicpc.net/problem/2669
import sys
sys.stdin = open('2669_input.txt', 'r')

g = [[0]*101 for _ in range(101)]

for _ in range(4):
    i, j, k, l = map(int, input().split())
    for x in range(i, k):
        for y in range(j, l):
            g[x][y] = 1

print(sum(map(sum, g)))

# 바뀐적 있을 때만 + 해준다