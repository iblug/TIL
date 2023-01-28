# 1269 대칭 차집합 https://www.acmicpc.net/problem/1269
import sys
sys.stdin = open('1269_input.txt', 'r')

_=input()
a = set(input().split())
b = set(input().split())
print(len(a^b))