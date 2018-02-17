from collections import Counter as C
c=C()
input()
print(sum(c.update(x) or c['D']==c['U'] and x=='U' for x in input()))
