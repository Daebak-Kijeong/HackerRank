# x+vt=y+wt
# x-y=(w-v)t
x,v,y,w=map(int,input().split())

a=x-y
b=w-v
print(['NO','YES'][a==0 or (b!=0 and a%b==0 and a*b>0)])