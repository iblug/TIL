# 3052 나머지 https://www.acmicpc.net/problem/3052
import sys
sys.stdin = open('3052_input.txt', 'r')

r = set()
for _ in range(10):
    r.add(int(input())%42)
print(len(r))














'''
# 예전 풀이
a=[]
for _ in range(10):
    x = int(input())%42
    if x not in a:
        a.append(x)
print(len(a))
'''