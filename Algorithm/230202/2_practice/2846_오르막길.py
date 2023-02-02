# 2846 오르막길 https://www.acmicpc.net/problem/2846
import sys
sys.stdin = open('2846_input.txt', 'r')

n = int(input())
p = list(map(int, input().split()))

step = 0
max_step = []
for i in range(n-1):
    if p[i+1] > p[i]:
        step += p[i+1] - p[i]
    else:
        max_step.append(step)
        step = 0
    # print('step:',step)
max_step.append(step)
# print(max_step)
print(max(max_step))
    
