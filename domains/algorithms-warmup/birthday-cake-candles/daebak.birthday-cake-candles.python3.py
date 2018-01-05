##birthdayCakeCandles
import sys
import itertools
def birthdayCakeCandles(n, ar):
    a = ar.count(max(ar)) #itertools모듈 >>> 각 인자들 반환
    for k,v in itertools.groupby(sorted(ar)):
        print(list(v))
    return a
    # Complete this function
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
