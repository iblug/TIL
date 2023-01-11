# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QKsLaAy0DFAUq&categoryId=AV5QKsLaAy0DFAUq&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1
# 신문 헤드라인

# print(input().upper())

import sys
sys.stdin = open('input.txt', 'r')

s = input()

result =''
for c in s:
    if  c.islower():
        result += chr(ord(c)-32)
    else:
        result += c

print(result)