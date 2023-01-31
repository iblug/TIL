# 10798 세로 읽기 https://www.acmicpc.net/problem/10798
import sys
sys.stdin = open('10798_input.txt', 'r')

data = []
for _ in range(5):
    lst = list(input())
    data.append(lst + ['']*(15-len(lst)))
print(*data, sep='\n')
for i in range(15):
    for j in range(5):
        print(data[j][i], end='')