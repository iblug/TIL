# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QQhbqA4QDFAUq&categoryId=AV5QQhbqA4QDFAUq&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1
# 최대수 구하기

T = int(input())

for t in range(1, T + 1):
    data = list(map(int, input().split()))
    print(f'#{t} {max(data)}')