from collections import Counter as C
input()
print(C(map(int,input().split())).most_common()[0][0])