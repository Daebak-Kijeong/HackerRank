n,k=map(int,input().split())
s=list(map(int,input().split()))
print(sum((s[a]+s[b])%k==0 for a in range(n) for b in range(a+1,n)))
