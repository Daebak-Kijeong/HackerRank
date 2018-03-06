n,k=map(int,input().split())
cs=list(map(int,input().split()))
bc=int(input())
ba=(sum(cs)-cs[k])/2
print(['%g'%(bc-ba),'Bon Appetit'][bc==ba])
