# 5576 콘테스트 https://www.acmicpc.net/problem/5576
import sys
sys.stdin = open('5576_input.txt', 'r')

# 44ms
import sys
input = sys.stdin.readline

sum1, sum2 = [], []

for _ in range(10):
    sum1.append(int(input()))
for _ in range(10):
    sum2.append(int(input()))
result1 = sum(sorted(sum1)[-3:])
result2 = sum(sorted(sum2)[-3:])
print(result1, result2) 















"""
# 44ms
import sys
input = sys.stdin.readline

w, k = [], []

for _ in range(10):
    w.append(int(input()))
for _ in range(10):
    k.append(int(input()))
w.sort()
k.sort()
ww = kk = 0
for _ in range(3):
    ww += w.pop()
    kk += k.pop()
print(ww, kk)


""" 
