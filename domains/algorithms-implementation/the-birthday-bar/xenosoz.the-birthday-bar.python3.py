N=int(input())
s=list(map(int,input().split()))
d,m=map(int,input().split())

print(sum(sum(s[i:i+m])==d for i in range(N-m+1)))
