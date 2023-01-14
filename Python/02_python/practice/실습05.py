
# 문제 1

data1 = input('문자열을 입력하세요 > ')
for i in range(len(data1)):
    if data1[i] == 'e':
        print(i)
        break
else:
    print(-1)

# 문제 2

data2 = input('문자열을 입력하세요 > ').split()
result = {}
for word2 in data2:
    result[word2] = result.get(word2, 0) + 1
for k2, v2 in result.items():
    print(k2, v2)

# 문제 3

data3 = list(input('문자열을 입력하세요 > ')) # 문자열을 list로 변환
for i3 in data3:
    if i3 == 'e':
        data3.remove('e') # 가장 왼쪽에 있는 e 제거
print(''.join(data3))

# 문제 4

data4, a4 = input('문자열을 입력하세요 > ').split()
cnt4 = 0
for i4 in data4:
    if i4 == a4:
        cnt4 += 1
print(cnt4)

# 문제 5

data5 = input('문자열을 입력하세요 > ').split()
print(f'{data5[0]}-{data5[1]}-{data5[2]}')

# 문제 6

data6 = int(input('양의 정수를 입력하세요 > '))

if data6 < 0:
    print(-1)
else:
    result = 0
    while data6 > 0:
        result += data6 % 10
        data6 //= 10
    else:
        print(result)