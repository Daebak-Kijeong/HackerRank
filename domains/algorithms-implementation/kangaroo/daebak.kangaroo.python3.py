##kangaroo
#input 0 3 4 2
#21 6 47 3
#2081 8403 9107 8400
#x1, x2 <= 10000
import sys

def kangaroo(x1, v1, x2, v2):
    a, b = x1, x2
    if (x1 < x2 and v1 > v2):
        try:
            for i in range(5000):
                for j in range(5000):
                    x1, x2 = a + i*v1, b + j*v2
                    if i == j and x1 == x2:
                        return "YES"
                    else:
                        pass

            else:
                return "NO"
        except:
            return "NO"

    else:
        return "NO"
# Complete this function
x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
