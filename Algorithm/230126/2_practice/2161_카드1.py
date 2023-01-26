# 2161 카드1 https://www.acmicpc.net/problem/2161

from collections import deque
q = deque([i for i in range(1, int(input())+1)])
while len(q) > 1:
    print(q.popleft(),end=' ')
    q.append(q.popleft())
print(q.popleft())