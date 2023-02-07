# 7568 덩치 https://www.acmicpc.net/problem/7568
import sys
sys.stdin = open('7568_input.txt', 'r')

n = int(input())
d = [tuple(map(int, input().split())) for _ in range(n)]
for i in range(n):
    cnt = 1
    for j in range(n):
        if d[i][0] < d[j][0] and d[i][1] < d[j][1]:
            cnt += 1
    print(cnt)



#