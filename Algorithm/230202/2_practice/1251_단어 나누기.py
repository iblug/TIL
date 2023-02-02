# 1251 단어 나누기 https://www.acmicpc.net/problem/1251
import sys
sys.stdin = open('1251_input.txt', 'r')

s = input()
l = len(s)
r = []
for i in range(1,l-1):
    for j in range(i+1, l):
        n1 = s[:i]
        n2 = s[i:j]
        n3 = s[j:]
        r.append(n1[::-1]+n2[::-1]+n3[::-1])
r.sort()
print(r[0])