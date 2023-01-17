# https://www.acmicpc.net/problem/1110
# 더하기 사이클

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
new = N
cnt = 0

while True:
    a, b = divmod(new, 10)
    new = 10*b + (a+b)%10
    cnt += 1
    if new == N:
        break

print(cnt)


# 해봤던 문제라서 좋아보이는 코드를 기억해놨다가 활용함
# 문자열로 해보기!