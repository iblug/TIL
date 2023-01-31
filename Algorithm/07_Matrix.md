# 이차원 리스트(matrix)
## 목차
1. 이차원 리스트
2. 입력 받기
3. 순회
4. 전치
5. 회전
## 학습 목표
* 이차원 리스트로 구성된 문제의 Input을 관리할 수 있다.
* 이차원 리스트의 순회를 할 수 있다.
* 이차원 리스트의 행과 열을 바꿔 관리할 수 있다.
* 이차원 리스트를 회전할 수 있다.
# 1. 이차원 리스트
* **리스트를 원소로 가지는 리스트**
* **행렬(matrix)**
## 특정 값으로 초기화 된 이차원 리스트 만들기
1. 직접 작성(4x3 행렬)
```py
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
```
2. 반복문으로 작성
  * 100x100 행렬
  ```py
  matrix = []

  for _ in range(100):
      matrix.append([0] * 100)
  ```
  * NxM
  ```py
  n = 4 # 행
  m = 3 # 열
  matrix = []

  for _ in range(n):
      matrix.append([0] * m)

  print(matrix)
  # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
  ```
3. 리스트 컴프리헨션으로 작성(NxM 행렬)
```py
n = 4 # 행
m = 3 # 열

matrix = [[0] * m for _ in range(n)]

print(matrix)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
```
  * *(주의!) 리스트 컴프리헨션 vs 리스트 곱셈연산*

# 2. 입력 받기
1. 행렬의 크기가 미리 주어지는 경우
```py
matrix = []

for _ in range(8)
    line = list(input())
    matrix.append(line)
```
```py
matrix = [list(input()) for _ in range(8)]
```
2. 행렬의 크기가 입력으로 주어지는 경우
```py
n, m = map(int, input().split()) # 8 7
matrix = []

for _ in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)
```
```py
n, m = map(int, input().split()) # 8 7
matrix = [list(map(int, input().split())) for _ in range(n)]
```

# 3. 순회
1. 이중 for문을 이용한 **행 우선 순회**
```py
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 0, 1, 2]
]

for i in range(3): # 행
    for j in range(4): # 열
        print(matrix[i][j], end=' ')
    print()
```
2. 이중 for문을 이용한 **열 우선 순회**
```py
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 0, 1, 2]
]

for i in range(4): # 열
    for j in range(3): # 행
        print(matrix[j][i], end=' ')
    print()
```
## 총합
1. 행 우선 순회를 이용해 이차원 리스트의 **총합** 구하기
```py
matrix = [
  [1, 1, 1, 1],
  [1, 1, 1, 1],
  [1, 1, 1, 1]
]

total = 0

for i in range(3):
  for j in range(4):
    tatal += matrix[i][j]

print(total)
# 12
```
2. Pythonic한 방법으로 이차원 리스트의 **총합** 구하기
```py
matrix = [
  [1, 1, 1, 1],
  [1, 1, 1, 1],
  [1, 1, 1, 1]
]

total = sum(map(sum, matrix))

print(total)
# 12
```
0. *각 행별, 열별 합 구하기*
```py
```
## 최대값
1. 행 우선 순회를 이용해 이차원 리스트의 **최댓값, 최솟값** 구하기
```py
matrix = [
  [0, 5, 3, 1],
  [4, 6, 10, 8],
  [9, -1, 1, 5]
]

# 최댓값
max_value = 0

for i in range(3):
    for j in range(4):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]

print(max_value)
# 10

# 최솟값
min_value = 1e9

for i in range(3):
    for j in range(4):
        if matrix[i][j] < min_value:
            if matrix[i][j] = matrix[i][j]

print(min_calue)
# -1
```
2. Pythonic한 방법으로 이차원 리스트의 **최댓값, 최솟값** 구하기
```py
matrix = [
  [0, 5, 3, 1],
  [4, 6, 10, 8],
  [9, -1, 1, 5]
]

max_value = max(map(max, matrix))
min_value = min(map(min, matrix))

print(max_value)
# 10
print(min_value)
# -1
```

# 4. 전치(transpose)
* 행렬의 행과 열을 서로 맞바꾸는 것
```py
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 0, 1, 2]
]

transposed_matrix = [[0] * 3 for _ in range(4)]

for i in range(4):
    for j in range(3):
        transposed_matrix[i][j] = matrix[j][i]
```

# 5. 회전
```py
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

n = 3
rotated_left_matrix = [[0] * n for _ in range(n)]
rotated_right_matrix = [[0] * n for _ in range(n)]
new_matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        rotated_left_matrix[i][j] = matrix[j][n-i-1] # 좌회전
        rotated_right_matrix[i][j] = matrix[n-j-1][i] # 우회전
        new_matrix[i][j] = matrix[n-j-1][n-j-1] # 180도

```

* *zip()*