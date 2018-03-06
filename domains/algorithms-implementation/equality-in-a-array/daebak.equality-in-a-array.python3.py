##equality-in-a-array
# n = 5
# arr = [1, 3, 3, 2, 1, 3]

import sys
from collections import Counter as C

def equalizeArray(arr):
    most_num = C(arr).most_common()
    a = most_num[0][0]
    b = most_num[0][1]
    # [a for i in range(b)]
    return len(arr) - b
    # Complete this function

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = equalizeArray(arr)
    print(result)