# 2592 대표값 https://www.acmicpc.net/problem/2592
import sys
sys.stdin = open('2592_input.txt', 'r')


# from collections import Counter
# d = [int(input()) for _ in range(10)]
# c = Counter(d)

# print(sum(d)//10)
# print(c.most_common(1)[0][0])

d = {}
sum_ = 0
for _ in range(10):
    num = int(input())
    sum_ += num
    d[num] = d.get(num, 0) + 1

print(sum_//10)
d = sorted(d.items(), key=lambda x: x[1])
print(d[-1][0])