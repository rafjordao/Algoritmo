S=0.0
X=str(input())
X=X.split()
X[0]=int(X[0])
X[1]=int(X[1])
while X[0]!=0 or X[1]!=0:
    if X[1]>0:
        S=float(X[0])
    expo=2
    fat=1
    N=X[1]-1
    for i in range(N):
        fat=fat*expo*(expo+1)
        if i%2==0:
            S=S-((X[0]**expo)/fat)
        else:
            S=S+((X[0]**expo)/fat)
        expo=expo+2
    print("%.6f"%(S))
    X=str(input())
    X=X.split()
    X[0]=int(X[0])
    X[1]=int(X[1])
    
