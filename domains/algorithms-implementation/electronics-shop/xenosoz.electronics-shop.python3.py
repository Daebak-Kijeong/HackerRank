from itertools import product as p
s,n,m = map(int,input().split())
k=list(map(int,input().split()))
u=list(map(int,input().split()))
print(max((a+b for a,b in p(k,u) if a+b<=s),default=-1))