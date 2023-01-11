# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5PjKXKALcDFAUq&categoryId=AV5PjKXKALcDFAUq&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1
# 1대1 가위바위보

a, b = map(int, input().split())
# if a - (b % 3) == 1:
#     print('A')
# else:
#     print('B')
print(('BA')[a - (b % 3) == 1])
# 0123456789