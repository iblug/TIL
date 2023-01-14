# 1. 모듈을 가져오는 것!
import random

# menu = ['햄버거', '국밥', '초밥']
# print(random.choice(menu))

# 로또 추첨 코드 작성
# random.sample(population, k)
# return a k length list
# the population sequence

# arr = [i for i in range(1, 46)]
arr = range(1, 46)
print(random.sample(arr, 6))
# [3, 6, 32, 24, 20, 18]
# [18, 7, 6, 35, 27, 30]


# shuffle




















# .sort() : 매서드
# return : None
numbers = [10, 2, 5]
result = numbers.sort()
print(result) # None
print(numbers)


# sorted() : 함수
# return ; 정렬된 리스트
numbers = [10, 2, 5]
result = sorted(numbers)
print(result) # [2, 5, 10]