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
# 4. 전치
# 5. 회전