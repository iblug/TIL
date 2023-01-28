# 20001 고무오리 디버깅 https://www.acmicpc.net/problem/20001
import sys
sys.stdin = open('20001_input.txt', 'r', encoding='utf-8')
input = sys.stdin.readline
c = input()
if c == '고무오리 디버깅 시작':
    stack = []
    while True:
        c = input()
        if c == '문제':
            stack.append('문제')
        elif c == '고무오리':
            if stack:
                stack.pop()
            else:
                stack.append('문제')
                stack.append('문제')
        elif c == '고무오리 디버깅 끝':
            break
    if stack:
        print('힝구')
    else:
        print('고무오리야 사랑해')