N=int(input())
l=list(map(int,input().split()))
print(sum(x>0 for x in l)/N)
print(sum(x<0 for x in l)/N)
print(sum(x==0 for x in l)/N)
