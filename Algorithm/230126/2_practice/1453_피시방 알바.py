# 1453 피시방 알바 https://www.acmicpc.net/problem/1453

seat = [0] * 101

n = int(input())
cnt = 0
x = list(map(int, input().split()))

for i in x:
    if seat[i] == 0:
        seat[i] = 1
    else:
        cnt +=1
print(cnt)

# set로 풀어보기