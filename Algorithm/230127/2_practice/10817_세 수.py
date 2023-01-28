# 10817 세 수 https://www.acmicpc.net/problem/10817
import sys
sys.stdin = open('10817_input.txt', 'r')

d = list(map(int, input().split()))
d.sort()
print(d[1])



'''
import heapq
# def m(x):
#     return -int(x)
# h = list(map(m, input().split()))
h = list(map(lambda x: -int(x), input().split()))
heapq.heapify(h)
heapq.heappop(h)
print(-heapq.heappop(h))
'''