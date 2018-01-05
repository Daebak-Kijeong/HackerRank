x=list(zip(input().split(),input().split()))
A=sum(int(a)>int(b)for a,b in x)
B=sum(int(a)<int(b)for a,b in x)
print(A,B)