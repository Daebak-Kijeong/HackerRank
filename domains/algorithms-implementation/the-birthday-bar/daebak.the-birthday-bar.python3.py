##the-birthday-bar
# n = 5
# s = [1,2,1,3,2]
# d,m = [3,2]
# n = 1
# s = [4]
# d,m = [4,1]
# n = 19
# s = [2,5,1,3,4,4,3,5,1,1,2,1,4,1,3,3,4,2,1]
# d,m = 18,7
import sys
from functools import reduce
def solve(n, s, d, m):
    li2 = []
    li = [s[i:m + i] for i in range(int(n))]
    for j in li:
        # print(j)
        if len(j) > 1 and len(j) == m and reduce(lambda x, y: x + y, j) == d:
            li2.append(j)

        elif len(j) == 1 and len(j) == m and reduce(lambda x, y: x + y, j) == d:
            li2.append(j)
        else:
            pass
    li2 = list(map(tuple, li2))
    li2 = set(li2)

    return len(li2)
    # Complete this function

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)