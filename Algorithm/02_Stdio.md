# 기본입출력
## 목차
1. 입력 활용 예시(input)
2. 출력 활용 예시(print)

# 1. 입력 활용 예시(input)
```py
# 문자열 입력 받기
a = input

# 한 개 숫자 입력 받기
b = int(input())

# 여러 개 숫자 입력 받기
d, e = map(int, input().split())
f, g, h = map(float, input().split())
```

# 2. 출력 활용 예시(print)
```py
print('hyper')
# hyper

a = 'hyper'
b = 'growth'
print(a, b)
# hyper growth
print(a, end='@')
print(b)
# hyper@growth
print(a, b, sep='\n')
'''
hyper
growth
'''
```