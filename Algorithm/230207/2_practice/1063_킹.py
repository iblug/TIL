# 1063 킹 https://www.acmicpc.net/problem/1063
import sys
sys.stdin = open('1063_input.txt', 'r')

def con(x):
    return (int(x[1]), ord(x[0]))
    
def re(x):
    return chr(x[1]) + str(x[0])

d = {
    'R': (0, 1),
    'L': (0, -1),
    'B': (-1, 0),
    'T': (1, 0),
    'RT': (1, 1),
    'LT': (1, -1),
    'RB': (-1, 1),
    'LB': (-1, -1)
}

k, s, n = input().split()

k = con(k)
s = con(s)

for _ in range(int(n)):
    dir = input()
    nx = k[0] + d[dir][0]
    ny = k[1] + d[dir][1]
    if 0 < nx <= 8 and 65 <= ny < 73:
        if s == (nx, ny):
            sx = s[0] + d[dir][0]
            sy = s[1] + d[dir][1]
            if 0 < sx <= 8 and 65 <= sy < 73:
                s = (sx, sy)
                k = (nx, ny)
        else:
            k = (nx, ny)

print(re(k), re(s), sep='\n')