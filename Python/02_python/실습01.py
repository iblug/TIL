# 문제1
num = int(input('숫자를 입력해주세요 > '))
print(num + 10)

# 문제2
food = input('좋아하는 음식을 입력해주세요 > ')
print('좋아하는 음식 : ' + food)

# 문제3
name = input('이름을 입력해주세요 > ')
year = int(input('태어난 년도를 입력해주세요 > '))
age = 2023 - year + 1
print('저의 이름은 ' + name + '이고, 올해 나이는 ' + str(age) + '세 입니다.')

# 문제4
a = input('첫 번째 문장을 입력해주세요 > ')
b = input('두 번째 문장을 입력해주세요 > ')
print(a + b)

# 문제5
n = int(input('숫자를 입력해주세요 > '))
print(n * -1)

# 문제6
n1 = int(input('첫 번째 숫자를 입력해주세요 > '))
n2 = int(input('두 번째 숫자를 입력해주세요 > '))
print('더하기 연산 :', n1 + n2)
print('빼기 연산 :', n1 - n2)
print('곱하기 연산 :', n1 * n2)
print('몫 연산 :', n1 // n2)
print('나머지 연산 :', n1 % n2)

# 문제7
m1 = int(input('첫 번째 숫자를 입력해주세요 > '))
m2 = int(input('두 번째 숫자를 입력해주세요 > '))
m3 = int(input('세 번째 숫자를 입력해주세요 > '))
print((m1 + m2 + m3)/3)

# 문제8
arr = []
o1 = int(input('첫 번째 정수형 숫자를 입력해주세요 > '))
arr.append(o1)
o2 = int(input('두 번째 정수형 숫자를 입력해주세요 > '))
arr.append(o2)
o3 = int(input('세 번째 정수형 숫자를 입력해주세요 > '))
arr.append(o3)
o4 = int(input('네 번째 정수형 숫자를 입력해주세요 > '))
arr.append(o4)
o5 = int(input('다섯 번째 정수형 숫자를 입력해주세요 > '))
arr.append(o5)
print(arr)

# 문제9
p1 = input('문자열을 입력해주세요 > ')
p2 = int(input('정수형 숫자를 입력해주세요 > '))
print(p1 * p2)

# 문제10
result = 0
result += int(input('첫 번째 정수형 숫자를 입력해주세요 > '))
print(result)
result += int(input('두 번째 정수형 숫자를 입력해주세요 > '))
print(result)
result += int(input('세 번째 정수형 숫자를 입력해주세요 > '))
print(result)
result += int(input('네 번째 정수형 숫자를 입력해주세요 > '))
print(result)
result += int(input('다섯 번째 정수형 숫자를 입력해주세요 > '))
print(result)


#s = ['첫', '두', '세', '네', '다섯']
#result = 0

#for i in s:
#    result += int(input(i+' 번째 정수형 숫자를 입력해주세요 > '))
#    print(result)