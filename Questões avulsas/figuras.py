import sys
total=sys.stdin.readline()
total=int(total)
J=M=TotalJ=TotalM=0
SJ=[]
SM=[]
for i in range(total):
    i=sys.stdin.readline()
    i=int(i)
    if i%2==0:
        J=J+1
        if i not in SJ:
            TotalJ=TotalJ+i
            SJ.append(i)
    else:
        M=M+1
        if i not in SM:
            TotalM=TotalM+i
            SM.append(i)
print(J)
print(M)
if TotalJ>TotalM:
    print(TotalJ)
else:
    print(TotalM)
