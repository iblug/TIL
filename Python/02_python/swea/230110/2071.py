# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QRnJqA5cDFAUq&categoryId=AV5QRnJqA5cDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1
# 평균값 구하기

T = int(input())

for t in range(1, T + 1):
    data = list(map(int, input().split()))
    avg = round(sum(data)/len(data))
    print(f'#{t} {avg}')
