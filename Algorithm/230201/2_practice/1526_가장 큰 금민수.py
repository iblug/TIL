# 1526 가장 큰 금민수 https://www.acmicpc.net/problem/1526
import sys
sys.stdin = open('1526_input.txt', 'r')
# 176ms
# n = int(input())

# while True:
#     n_ = str(n)
#     n_ = n_.replace('7', '')
#     n_ = n_.replace('4', '')
#     if n_:
#         n -= 1
#     else:
#         print(n)
#         break

# 164ms
n = int(input())
data = ['0', '1', '2', '3', '5', '6', '8', '9']

while True:
    n_ = str(n)
    for d in data:
        if d in n_:
            n -= 1
            break
    else:
        print(n)
        break