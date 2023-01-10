# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QGNvKAtEDFAUq&categoryId=AV5QGNvKAtEDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=2
# 몫과 나머지 출력하기

T = int(input())

for t in range(1, T + 1):
    a, b = map(int, input().split())
    print(f'#{t}',*divmod(a, b))