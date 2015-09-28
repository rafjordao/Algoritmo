import math
n=int(input())
m=int(input())
a=b=x=c=d=x=y=0
while n>=1 and m>=1:
    if (n*m)%2==0:
        t=((n*m)/2)*(n*m)+((n*m)/2)
    else:
        t=math.ceil((n*m)/2)*(n*m)
    for i in range(n):
        a+=(m*i)+1
        b+=(m*i)+m
        x+=(m*i)+i+1
        y+=(n*m)-(i*m)-i
    for j in range(m):
        c+=j+1
        d+=(m*n)-j
    result=(t-(x+y)+(a*b)-(c*d))/(n*m)
    print("%.2f"%(result))
    n=int(input())
    m=int(input())
    a=b=x=c=d=x=y=0
result=0.0
print("%.2f"%(result))
