input()
l=list(map(int,input().split()))
m=max(l)
print(sum(m==x for x in l))