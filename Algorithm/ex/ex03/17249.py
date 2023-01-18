# https://www.acmicpc.net/problem/17249
# 태보태보 총난타

s = input()

f_l = s.find('(')
f_r = s.find(')')
print(s[:f_l].count('@'), s[f_r:].count('@'))
