# 1225 이상한 곱셉 https://www.acmicpc.net/problem/1225
import sys
# sys.stdin = open('Algorithm/test/2_practice/1225_input.txt', 'r')
sys.stdin = open('1225_input.txt', 'r')


a, b = input().split()
sum_a = sum(map(int, a))
sum_b = sum(map(int, b))
print(sum_a * sum_b)

