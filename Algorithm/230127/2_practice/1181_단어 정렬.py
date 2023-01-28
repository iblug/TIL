# 1181 단어 정렬 https://www.acmicpc.net/problem/1181
import sys
sys.stdin = open('1181_input.txt', 'r')

import sys
input = sys.stdin.readline

n = int(input())
d = set(input().rstrip() for _ in range(n))
r = sorted(d, key=lambda x: (len(x), x))
print('\n'.join(r))
