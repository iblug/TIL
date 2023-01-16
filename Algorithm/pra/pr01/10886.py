# https://www.acmicpc.net/problem/10886
# 0 = not cute / 1 = cute

import sys
import time
sys.stdin = open('input.txt', 'r')


n = int(input())
start = time.time()
'''
s = ''
for _ in range(n):
    s += input()
    # s += sys.stdin.readline().rstrip()
# print(s)
# print(s.count('0'))
if s.count('0') > n // 2:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')

'''
# 리스트를 쓰거나 변수 들어올때마다 cnt하자

cnt = 0
for _ in range(n):
    if input() == '0':
        cnt = 1
if cnt > n // 2:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')


end = time.time()
print(end - start)
