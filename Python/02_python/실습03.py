# 문제 1 절대값
a = int(input('정수를 입력하세요 > '))
if a >= 0:
    print(a)
else:
    print(-a)

###########################################

# 문제 2 리스트의 길이

number_list = [1, 2, 3, 4, 5]
# number_list = []
b = 0
for _ in number_list :
    b += 1
print(b)

###########################################

# 문제 3 리스트 합

number_list = [1, 2, 3, 4, 5]
# number_list = [-1, -2, -3, -4, -5]
c = 0
for i in number_list:
    c += i
print(c)

###########################################

# 문제 4 리스트 평균

number_list = [2, 4, 6]
# number_list = [2, 3, 5, 7]
d = 0
dl = 0
for i in number_list:
    d += i
    dl += 1
print(d/dl)

###########################################

# 문제 5 리스트 곱

number_list = [1, 2, 3, 4, 5]
# number_list = [-1, -2, 3]
e = 1
for i in number_list:
    e *= i
print(e)

###########################################

# 문제 6 리스트 가장 큰 수

number_list = [1, 2, 3, 4, 5]
# number_list = [1, 1, 1]

fmax = -1
for i in number_list:
    if i > fmax:
        fmax = i
print(fmax)

###########################################

# 문제 7 리스트 가장 작은 수

number_list = [1, 2, 3, 4, 5]
# number_list = [5, 5, 5, 2]

gmin = number_list[0]
for i in number_list:
    if i < gmin:
        gmin = i
print(gmin)