# https://www.acmicpc.net/problem/2506
# 점수계산

import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
r = input().split()
sum_ = 0
s = 0
for i in r:
    if i == '1':
        s +=1
        sum_ += s
    else:
        s = 0
print(sum_)

#######

# while 써보기

