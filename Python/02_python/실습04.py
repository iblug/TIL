# 문제 1 e 개수 출력
a = input('문자열을 입력하세요 > ')
count1 = 0
for i in a:
    if i == 'e':
        count1 += 1
print(count1)

##############################################

# 문제 2 알파벳 모음 개수
mo = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
b = input('문자열을 입력하세요 > ')
count2 = 0

for i in mo:
    for j in b:
        if i == j:
            count2 += 1

print(count2)

##############################################

# 문제 3 딕셔너리 출력 - 따옴표 중첩 주의!!

dict_variable = {
    '이름': '정우영',
    '생년': '2000',
    '회사': '하이퍼그로스',
}

##
print(f'나이 : {2023 - int(dict_variable["생년"])}세')

##############################################

# 문제 4 딕셔너리 입력 저장
person4 = {}
person4['이름'] = input('이름을 입력하세요 > ')
person4['전화번호'] = input('전화번호를 입력하세요 > ')
person4['거주지'] = input('거주지를 입력하세요 > ')

print(person4)
for key in person4:
    print(f'{key} : {person4[key]}')

##############################################

# 문제 5 딕셔너리 in 딕셔너리

person5 = {}
name5 = input('이름을 입력하세요 > ')
person5[name5] = {}
person5[name5]['전화번호'] = input('전화번호를 입력하세요 > ')
person5[name5]['이메일'] = input('이메일를 입력하세요 > ')
person5[name5]['거주지'] = input('거주지를 입력하세요 > ')

print(person5)

##############################################

# 문제 6 개수 개별 출력
data = {}
c = input('문자열을 입력하세요 > ')
for i in c:
    if i not in data:
        data[i] = 0
    data[i] += 1
for k, v in data.items():
    print(k, v)
