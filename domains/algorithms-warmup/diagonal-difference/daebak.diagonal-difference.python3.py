import sys
from functools import reduce

def diagonalDifference(a):

    A = 0
    for i in range(n):
        A += a[i][i]

    B = 0
    for i in range(n):
        B += a[i][n-i-1]

        # x = a[0][0] + a[1][1] + a[2][2]
        # y = a[0][2] + a[1][1] + a[2][0]

    return abs(A-B) #abs는 절대값
    # Complete this function

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
        a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
        a.append(a_t)
    result = diagonalDifference(a)
    print(result)