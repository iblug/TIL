# https://www.acmicpc.net/problem/10988
# 팰린드롬인지 확인하기

import sys
sys.stdin = open('input.txt', 'r')
a = input()
print('01'[a==a[::-1]])

# while 써보기

s = 'baekjoon'

start = 0
end = len(s)-1
while start<end:
    if s[start] != s[end-start]:
        print(0)
        break
    start += 1
else:
    print(1)