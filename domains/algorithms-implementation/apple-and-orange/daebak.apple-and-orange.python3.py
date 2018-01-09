##apple-and-orange
#7 11
#5 15
#3 2
#-2 2 1
#5 -6
import sys

def appleAndOrange(s, t, a, b, apple, orange):
    result_A = []
    result_B = []
    for i in apple:
        if (i + a) >= s and (i + a) <= t:
            result_A.append(i)
    for j in orange:
        if (j + b) >= s and (j + b) <= t:
            result_B.append(j)
    result = (len(result_A), len(result_B))
    return result
    # Complete this function

if __name__ == "__main__":
    s, t = input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = input().strip().split(' ')
    m, n = [int(m), int(n)]
    apple = list(map(int, input().strip().split(' ')))
    orange = list(map(int, input().strip().split(' ')))
    result = appleAndOrange(s, t, a, b, apple, orange)
    print ("\n".join(map(str, result)))