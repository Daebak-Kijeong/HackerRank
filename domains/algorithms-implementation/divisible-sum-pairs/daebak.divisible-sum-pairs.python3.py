##divisible-sum-pairs
# n, k = 6, 3
# ar = [1, 3, 2, 6, 1, 2]
'''
100 22
43 95 51 55 40 86 65 81 51 20 47 50 65 53 23 78 75 75 47 73 25 27 14 8 26 58 95 28 3 23 48 69 26 3 73 52 34 7 40 33 56 98 71 29 70 71 28 12 18 49 19 25 2 18 15 41 51 42 46 19 98 56 54 98 72 25 16 49 34 99 48 93 64 44 50 91 44 17 63 27 3 65 75 19 68 30 43 37 72 54 82 92 37 52 72 62 3 88 82 71
216
num = "43 95 51 55 40 86 65 81 51 20 47 50 65 53 23 78 75 75 47 73 25 27 14 8 26 58 95 28 3 23 48 69 26 3 73 52 34 7 40 33 56 98 71 29 70 71 28 12 18 49 19 25 2 18 15 41 51 42 46 19 98 56 54 98 72 25 16 49 34 99 48 93 64 44 50 91 44 17 63 27 3 65 75 19 68 30 43 37 72 54 82 92 37 52 72 62 3 88 82 71"
ar = list(map(int, num.split()))
n,k = 100,22
'''
import sys

def divisibleSumPairs(n, k, ar):

    li = []
    i = 0
    for x in range(101):
        for y in range(101):
            try:
                if x < y and (ar[x]+ar[y])%k ==0:
                    # print((ar[x],ar[y]),i)
                    li.append((ar[x], ar[y]))
            except IndexError:
                pass
        i += 1

    return len(li)
    # Complete this function

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)