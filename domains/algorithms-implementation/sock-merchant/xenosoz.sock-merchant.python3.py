from collections import Counter as C
input()
print(sum(x//2 for x in C(input().split()).values()))
