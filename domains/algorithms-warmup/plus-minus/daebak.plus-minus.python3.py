import sys


def plusMinus(arr):
    A = [x for x in arr if x > 0]
    B = [x for x in arr if x < 0]
    C = [x for x in arr if x == 0]

    A2 = round(len(A) / n, 6)
    B2 = round(len(B) / n, 6)
    C2 = round(len(C) / n, 6)

    return ('%.6f' %A2 + "\n" +  '%.6f' %B2 + "\n" + '%.6f' %C2)

    # Complete this function

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    print(plusMinus(arr))