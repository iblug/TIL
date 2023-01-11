# input.txt 파일을 생성하고, 입력을 작성해주세요.
# 코드를 알고리즘 사이트에 제출할 때 아래 두 줄은 주석처리 해주세요.
import sys
sys.stdin = open('./input.txt', 'r')
# 이하 입력 코드


# 문제 1 공백으로 구분된 정수

data1 = list(map(int, input().split()))
print(*data1)

# 문제 2 공백으로 구분된 문자열

data2 = input().split()
print(' '.join(data2))

# 문제 3 테스트 케이스 수와 입력 줄 수가 주어지는 입력

T3 = int(input())
for t3 in range(1, T3 + 1):
    N3 = int(input())
    for n3 in range(N3):
        data3 = int(input())
        print(data3)

# 문제 4 테스트 케이스 수와 입력 줄 수가 주어지는 입력

T4 = int(input())
for t4 in range(1, T4 + 1):
    N4 = int(input())
    for n4 in range(N4):
        a4, b4 = list(map(int, input().split()))
        print(a4, b4)

# 문제 5 테스트 케이스 수와 입력 줄 수가 주어지는 입력

T5 = int(input())
for t5 in range(1, T5 + 1):
    N5 = int(input())
    for n5 in range(N5):
        data5 = input().split()
        print(' '.join(data5))

# 문제 6 테스트 케이스 수와 입력 줄 수가 주어지는 입력

T6 = int(input())
for t6 in range(1, T6 + 1):
    N6 = int(input())
    for n6 in range(N6):
        data6 = list(map(int, input().split()))
        print(*data6)

# 문제 7 테스트 케이스 수와 입력 줄 수가 주어지는 입력

T7, N7 = list(map(int, input().split()))
for t7 in range(1, T7 + 1):
    for n7 in range(N7):
        data7 = int(input())
        print(data7)

# 문제 8 테스트 케이스 수와 입력 줄 수가 주어지는 입력

T8, N8 = list(map(int, input().split()))
for t8 in range(1, T8 + 1):
    for n8 in range(N8):
        a8, b8 = list(map(int, input().split()))
        print(a8, b8)

# 문제 9 테스트 케이스 수와 입력 줄 수가 주어지는 입력

T9, N9 = list(map(int, input().split()))
for t9 in range(1, T9 + 1):
    for n9 in range(N9):
        data9 = list(map(int, input().split())) 
        for d9 in data9:
            print(d9, end=' ')
        print()