s,t,a,b,m,n=map(int,' '.join([input(),input(),input()]).split())
r=range(s,t+1)
print(sum((a+d)in r for d in map(int,input().split())))
print(sum((b+d)in r for d in map(int,input().split())))
