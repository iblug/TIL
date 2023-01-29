# 이진 탐색(Binary Search)
* 순차 탐색(Sequential Search): 리스트 안에 있는 특정한 **데이터를 찾기 위해 앞에서 부터 데이터를 하나씩 확인**하는 방법
* 이진 탐색(Binary Search): 정렬되어 있는 리스트에서 **탐색 범위를 절반씩 좁혀가며 데이터를 탐색**하는 방법
  * 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정

## 이진 탐색 동작 예시
* ...

## 이진 탐색의 시간 복잡도
* 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 **연산 횟수는** log<sub>2</sub>N**에 비례**
* 다시 말해 이진 탐색은 탐색 범위를 절반씩 줄이며, 시간 복잡도는 **O(logN)**을 보장

## 이진 탐색 소스코드: 재귀적 구현
```py
# 7-2 189
# 이진 탐색 소스코드 구현 (재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)
    
# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)
'''
10 7
1 3 5 7 9 11 13 15 17 19

4
'''
'''
10 7
1 3 5 6 9 11 13 15 17 19

원소가 존재하지 않습니다.
'''
```

## 이진 탐색 소스코드: 반복문 구현
```py
# 7-3 190
# 이진 탐색 소스코드 구현 (반복문)
def binary_search(arry, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

## 이하 위의 코드와 같음
```

# 파이썬 이진 탐색 라이브러리
* [bisect](18_Useful_Standard_Library.md#bisect)

# 파라메트릭 서치(Parametric Search)
* **파라메트릭 서치**란 <u>최적화 문제를 결정 문제('예' 혹은 '아니오')로 바꾸어 해결하는 기법</u>
  * ex) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
* 일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 **이진 탐색을 이용하여 해결** 가능

# <문제> 떡볶이 떡 만들기
* 201

|입력|출력|
|-|-|
|4 6<br>19 15 10 17|15|

* 나의 답
```py
import sys
sys.stdin = open('input.txt', 'r')

def bin_search(arr, start, end):
    if start > end:
        return max(result)
    mid = (start + end) // 2
    cnt = 0
    for i in arr:
        if i > mid:
            cnt += i - mid
    if cnt < m:
        return bin_search(arr, start, mid - 1)
    else:
        result.append(mid)
        return bin_search(arr, mid + 1, end)

n, m = map(int, input().split())
data = list(map(int, input().split()))
result = []
print(bin_search(data, 0, max(data)))
```

* 예시 답
    * 적절한 높이를 찾을 때까지 이진 탐색을 수행하여 높이 H를 반복해서 조정
    * '현재 이 높이로 자르면 조건을 만족할 수 있는가?'를 확인한 뒤에 <u>조건의 만족 여부('예' 혹은 '아니오')에 따라서 탐색 범위를 좁혀서 해결</u>할 수 있음
    * 절단기의 높이는 0부터 10억까지의 정수 중 하나
        * 이렇게 큰 범위를 보면 가장 먼저 **이진 탐색**을 떠올려야 함
    * 문제에서 제시된 예시를 통해 그림으로 이해...
    * 중간점의 값은 <u>시간이 지날수록 **'최적화된 값**</u>이 되기 때문에, 과정을 반복하면서 얻을 수 있는 떡의 길이 합이 필요한 떡의 길이보다 크거나 같을 때마다 **중간점의 값을 기록**하면 됨


```py
# 7-8 205
# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력
n, m = list(map(int, input().split(' ')))
# 각 떡의 개별 높이 정보를 입력
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행 (반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡볶이 양 계산
        if x > mid:
            total += x - mid
    # 떡볶이 양이 부족한 경우 더 많이 자르기 (오른쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡볶이 양이 충분한 경우 덜 자르기 (왼쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

# 정답 출력
print(result)
```

# <문제> 정렬된 배열에서 특정 수의 개수 구하기
* 367 27 

|입력|출력|
|-|-|
|7 2<br>1 1 2 2 2 2 3|4|
|7 4<br>1 1 2 2 2 2 3|-1|

* 나의 답

```py
import bisect

def find_(data, x):
    return bisect.bisect_right(data, x) - bisect.bisect_left(data, x)

n, x = map(int, input().split())
data = list(map(int, input().split()))
result = find_(data, x)
if result:
    print(result)
else:
    print(-1)
```

* 예시 답
    * 시간 복잡도 **$O(logN)$**으로 동작하는 알고리즘을 요구
        * 일반적인 <u>선형 탐색(Linear Search)로는 시간 초과 판정</u>을 받음
        * 하지만 데이터가 정렬되어 있기 때문에 **이진 탐색을 수행**할 수 있음
    * 특정 값이 등장하는 첫 번째 위치와 마지막 위치를 찾아 위치 차이를 계산해 문제를 해결할 수 있음

```py
# 15-1 558 27-2 
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = map(int, input().split()) # 데이터의 개수 N, 찾고자 하는 값 x 입력 받기
array = list(map(int, input().split())) # 전체 데이터 입력 받기

# 값이 [x, x] 범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
# 값이 x인 원소가 존재한다면
else:
    print(count)
```

* bisect 없이?
```py
# 556 27-1  
```