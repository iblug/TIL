
# 문제 1

data1 = int(input('# 정수를 출력하세요.\n'))
print(data1)

# 문제 2
 
data2 = input('# 단어를 구분해서 출력하세요.\n').split()
print(' '.join(data2))

# 문제 3

t3 = int(input('# 테스트 케이스 마다 입력 값을 그대로 출력하세요.\n'))

for _ in range(1, t3 + 1):
    print(int(input()))
    pass

# 문제 4

data4 = list(map(int, input().spilt()))
print(*data4)

# 문제 5

num5_1, num5_2 = map(int, input().split())
print(num5_1, num5_2)

# 문제 6

data6 = input().split()
print(*data6)

# 문제 7

t7 = int(input())
for _ in range(t7):
    data7 = list(map(int, input().split()))
    print(*data7)

# 문제 8

t8 = int(input())
for _ in range(t8):
    data8 = list(map(int, input().split()))
    print(*data8)