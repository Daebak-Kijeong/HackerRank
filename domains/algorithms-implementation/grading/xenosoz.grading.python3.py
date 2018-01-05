N=int(input())
print('\n'.join(str((x,(x+4)//5*5)[x%5in[0,4,3]and x>=38]) for x in (int(input()) for i in range(N))))