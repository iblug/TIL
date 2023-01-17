# https://www.acmicpc.net/problem/10871
# X보다 작은수

import sys
sys.stdin = open('input.txt', 'r')

n, x = map(int, input().split())
a = list(map(int, input().split()))

for num in a:
    if num < x:
        print(num,end=' ')

# list에 넣고 print(*result)로 출력하는 방법도 있음