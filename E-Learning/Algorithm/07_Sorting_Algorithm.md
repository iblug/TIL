# 정렬 알고리즘 비교

|정렬 알고리즘|평균 시간 복잡도|공간 복잡도|특징|
|:-:|:-:|:-:|:-:|
|선택 정렬|O(N<sup>2</sup>)|O(N)|아이디어가 매우 간단함|
|삽입 정렬|O(N<sup>2</sup>)|O(N)|데이터가 거의 정렬되어 있을 때는 가장 빠름|
|퀵 정렬|O(NlogN)|O(N)|대부분의 경우에 적합하며, 충분히 빠름|
|계수 정렬|O(N+K)|O(N+K)|데이터의 크기가 한정되어 있는 경우에만 사용이 가능하지만 매우 빠르게 동작|
* 대부분의 프로그래밍 언어에서 지원하는 <u>표준 정렬 라이브러리는 최악의 경우에도 </u>**<u>O(NlogN)</u>**<u>을 보장</u>하도록 설계

## 수행 시간 비교
* 선택 정렬과 기본 정렬 라이브러리
```py
from random import randint
import time

# 배열에 10,000개의 정수를 삽입
array = []
for _ in range(10000):
    # 1부터 100 사이의 랜덤한 정수
    array.append(randint(1, 100))

# 선택 정렬 프로그램 성능 측정
start_time = time.time()

# 선택 정렬 프로그램 소스코드
for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

# 측정 종료
end_time = time.time()
# 수행 시간 출력
print('선택 정렬 성능 측정:', end_time - start_time)

# 배열을 다시 무작위 데이터로 초기화
array = []
for _ in range(10000):
    # 1부터 100 사이의 랜덤한 정수
    array.append(randint(1, 100))

# 기본 정렬 라이브러리 성능 측정
start_time = time.time()

# 기본 정렬 라이브러리 사용
array.sort()

# 측정 종료
end_time = time.time()
# 수행 시간 출력
print('기본 정렬 라이브러리 성능 측정:', end_time - start_time)
'''
선택 정렬 성능 측정: 2.3429102897644043
기본 정렬 라이브러리 성능 측정: 0.0
'''
```

# 문제풀이

* 두 배열의 원소 교체 182 6-12

## 문제 해결 아이디어
* **핵심 아이디어**: <u>매번 배열 A에서 가장 작은 원소를 골라서, 배열 B에서 가장 큰 원소와 교체
* 가장 먼저 배열 A와 B가 주어지면 A에 대해 오름차순 정렬하고, B에 대하여 내림차순 정렬
* 이후에 두 배열의 원소를 첫 번째 인덱스부터 차례로 확인하면서 A의 원소가 B의 원소보다 작을 때에만 교체를 수행
* 이 문제에서는 두 배열의 원소가 최대 100,000개까지 입력될 수 있으므로, 최악의 경우 **O(NlogN)**을 보장하는 정렬 알고리즘을 이용