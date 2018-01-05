import sys

from functools import reduce
def aVeryBigSum(n, ar):
    return reduce(lambda x, y: x + y, ar, 0) #lambda함수= 인자 : 표현식 / list(map(함수, 리스트)) / reduce(함수, 순서형 자료)
    # Complete this function

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)