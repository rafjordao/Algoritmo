n=int(input())
while n>0 and n<=47:
    a=0
    b=1
    print(a,end="")
    for i in range(n-1):
        aux=a
        a=b
        b=aux+b
        print(" %d"%(a),end="")
    print("")
    n=int(input())
