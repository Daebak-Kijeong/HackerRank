from collections import Counter
input()
print(sum(v for k,v in Counter(input().split()).most_common()[1:]))
