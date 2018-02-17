##cats-and-a-mouse
#x축에 고양이A와 고양이B, 쥐C가 있다.
#x는 고양이A의 위치, y는 고양이B의 위치, z는 쥐C의 위치다.
# q = 3
# x,y,z = 1, 2, 3
# # x,y,z = 1, 3, 2
# # x,y,z = 2, 1, 3
# q = 4
# x,y,z = 1, 4, 2
# q = 5
# x,y,z = 1, 5, 3

import sys

def catAndMouse(x, y, z):
    if abs(z - x) < abs(z - y):
        # print("Cat A")
        return("Cat A")
    elif abs(z - x) > abs(z - y):
        # print("Cat B")
        return("Cat B")
    elif abs(z - x) == abs(z - y):
        # print("Mouse C")
        return("Mouse C")

    # Complete this function

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        x, y, z = input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]
        result = catAndMouse(x, y, z)
        print ("".join(map(str, result)))

