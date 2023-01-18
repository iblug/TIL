# https://www.acmicpc.net/problem/2789
# 유학 금지

import sys
sys.stdin = open('input.txt', 'r')

data = 'CAMBRIDGE'
a = input()

# r = ''
# for i in a:
#     if i not in data:
#         r += i
# print(r)
for i in data:
    a = a.replace(i, '')
print(a)