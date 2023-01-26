# 9012 괄호 https://www.acmicpc.net/problem/9012

n = int(input())

for _ in range(n):
    d = []
    arr = input()
    for a in arr:
        if a == '(':
            d.append(a)
        elif a == ')':
            if d:
                d.pop()
            else:
                print('NO')
                break
    else:
        if d:
            print('NO')
        else:
            print('YES')