# https://www.acmicpc.net/problem/5622
# 다이얼

data = {
    'ABC' : 3, 
    'DEF' : 4, 
    'GHI' : 5, 
    'JKL' : 6, 
    'MNO' : 7, 
    'PQRS' : 8, 
    'TUV' : 9, 
    'WXYZ' : 10, 
}
n = input()
r = 0
for i in n:
    for j in data.keys():
        if i in j:
            r += data[j]
print(r)


# WA 입력시 W(7+1+2) + A(0+1+2)
""" 
data = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
n = input()

r = 0
for i in data:
    for j in n:
        if j in i:
            r += data.index(i) + 3
print(r) 
"""