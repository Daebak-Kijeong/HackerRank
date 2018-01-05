N=int(input())
print('\n'.join((' '*(N-1)+'#'*N)[i:i+N] for i in range(N)))
