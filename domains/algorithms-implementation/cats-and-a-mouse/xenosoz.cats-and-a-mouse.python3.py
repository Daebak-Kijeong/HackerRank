for i in range(int(input())):
    a,b,c=map(int,input().split())
    a=abs(a-c)
    b=abs(b-c)
    print(['Mouse C','Cat B','Cat A'][(a>b)-(a<b)])