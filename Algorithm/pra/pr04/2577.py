# https://www.acmicpc.net/problem/2577
# 숫자의 개수

import sys
sys.stdin = open('input.txt', 'r')

from collections import Counter

a = 1
for _ in range(3):
    a *= int(input())

d = Counter(str(a))

for i in range(10):
    print(d.get(str(i),0))
    


'''
a=int(input())
a*=int(input())
a*=int(input())
for i in range(10):
    print(str(a).count(str(i)))
    
'''