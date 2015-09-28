import sys
Imp=[0]*5
Par=[0]*5
P=0
I=0
for line in sys.stdin:
    if not line:
        sys.exit()
    line=int(line)
    if line%2==0:
        Par[P]=line
        P+=1
    else:
        Imp[I]=line
        I+=1
    if P==5:
        for i in range(P):
            print("par[%d] = %d"%(i,Par[i]))
        P=0
    if I==5:
        for i in range(I):
            print("impar[%d] = %d"%(i,Imp[i]))
        I=0
for i in range(I):
    print("impar[%d] = %d"%(i,Imp[i]))
for i in range(P):
    print("par[%d] = %d"%(i,Par[i]))
