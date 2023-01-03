# 실습1
a = int(input('정수를 입력하세요 > '))
if a > 0:
    print(True)
else:
    print(False)

# 실습2
b = int(input('첫 번째 정수를 입력하세요 > '))
c = int(input('두 번째 정수를 입력하세요 > '))
if b > c:
    print(b)
elif c > b:
    print(c)
else:
    print(False) 

# 실습3
d = int(input('정수를 입력하세요 > '))
if 1 < d < 10:
    print(True)
else:
    print(False)

# 실습4
e = int(input('정수를 입력하세요 > '))
if e > 0 and e%2 == 0:
    print(True)
else:
    print(False)

# 실습5
f = int(input('정수를 입력하세요 > '))
if 0 <= f <= 100:
    if f >= 60:
        print('합격')
    else:
        print('불합격')
else:
    print('에러')
    
# 실습6
g = input('문자열을 입력하세요 > ')
for i in g[::-1]:
    print(i)


# 실습7 오름차순
h1 = int(input('첫 번째 정수를 입력하세요 > '))
h2 = int(input('두 번째 정수를 입력하세요 > '))
if h1 < h2:
    for i in range(h1 + 1, h2):
        print(i)
elif h2 < h1:
    for i in range(h2 + 1, h1):
        print(i)
else:
    print(False)

# 실습8
m1 = int(input('첫 번째 정수를 입력하세요 > '))
m2 = int(input('두 번째 정수를 입력하세요 > '))
if m1 < m2:
    for i in range(m2 - 1, m1, -1):
        print(i, end=' ')
elif m2 < m1:
    for i in range(m1 - 1, m2, -1):
        print(i, end=' ')
else:
    print(False)

# 실습9 
n = int(input('정수를 입력하세요 > '))
if n >= 1:
    for i in range(1, n):
        if i % 2 == 1:
            print(i)
        else:
            continue
else:
    print(False)

# 실습10 구구단
for i in range(2, 10):
    for j in range(2, 10):
        print(f'{i} X {j} =', i * j)