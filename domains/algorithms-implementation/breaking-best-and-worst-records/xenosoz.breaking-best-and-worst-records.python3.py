N=int(input())
s=list(map(int,input().split()))
print(len(set(max(s[:i+1]) for i in range(N)))-1, len(set(min(s[:i+1]) for i in range(N)))-1)