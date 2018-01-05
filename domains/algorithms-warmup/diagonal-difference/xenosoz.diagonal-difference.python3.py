N=int(input())
print(abs(sum(((a//N==a%N)-(a//N+a%N+1==N))*int(b) for a,b in zip(range(N*N),' '.join(input() for i in range(N)).split()))))
