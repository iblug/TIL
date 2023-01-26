# 10101 삼각형 외우기 https://www.acmicpc.net/problem/10101

a,b,c = [int(input()) for _ in range(3)]

if a + b + c != 180:
    print('Error')
elif a == b == c == 60:
    print('Equilateral')
elif a == b or b == c or a == c:
    print('Isosceles')
else:
    print('Scalene')
