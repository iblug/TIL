
# 문제 1 

number1 = int(input())
print(number1)

# 문제 2

num1, num2 = list(map(int, input().split()))
print(num1, num2)

# 문제 3

number3 = list(map(int, input().split()))
for num in number3:
    print(num, end=' ')

# 문제 4

words1 = input().split()
print(' '.join(words1))

# 문제 5

numbers5 = list(map(int, input().split()))
print(*numbers5)

# 문제 6

nums6 = map(int, input().split())
print(*nums6)

# 문제 7
words7 = input().split()
print(' '.join(words7))

# 문제 8
nums8 = list(map(int, input().split()))
for num8 in nums8:
    print(num8, end=' ')

# 문제 9
nums9 = list(map(int, input().split()))
print(*nums9)