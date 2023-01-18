# https://www.acmicpc.net/problem/10809
# 알파벳 찾기

s = input()

a = 'abcdefghijklmnopqrstuvwxyz'
for i in a:
    print(s.find(i),end=' ')