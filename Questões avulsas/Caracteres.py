n=int(input())
while n!=0:
    S=str(input())
    S2=""
    for i in range(n-1,-1,-1):
        S2="%s%s"%(S2,S[i])
    print(S2)
    n=int(input())
