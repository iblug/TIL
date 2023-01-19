# https://www.acmicpc.net/problem/7785
# 회사에 있는 사람

################# 백준 1위!! ######
# 추출하고 정렬 => 속도 빠름 

import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
# print = sys.stdout.write # 오히려 느림

N = int(input())
is_in = {}
for _ in range(N):
    a, b = input().split()
    is_in[a] = b

result = [i for i in is_in if is_in[i] == 'enter']
# print(*result,sep='\n') # 출력 속도느림
print('\n'.join(sorted(result, reverse=True)))


# 딕셔너리로 풀어보기
""" import sys
input = sys.stdin.readline
print = sys.stdout.write

sys.stdin = open('input.txt', 'r')

N = int(input())
is_in = {}
for _ in range(N):
    a, b = input().split()
    is_in[a] = b
is_in = dict(sorted(is_in.items(), reverse=True))

for k, v in is_in.items():
    if v == 'enter':
        print(k+'\n') """


# readlines로 풀어보기?