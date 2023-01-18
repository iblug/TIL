# https://www.acmicpc.net/problem/2941
# 크로아디아 알파벳

import sys
sys.stdin = open('input.txt', 'r')

data = ['c=', 'c-', 'z=', 'd-', 'lj', 'nj', 's=', 'dz=']
s = input()
a = 0
for i in data:
    a += s.count(i)
print(len(s) - a)
# for i in data:
#     s = s.replace(i, '*')
# print(s, len(s))