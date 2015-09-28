import sys
def converte(n):
    n=n.split()
    for p in range(len(n)):
        n[p]=int(n[p])
    return n
IS=sys.stdin.readline()
IS=converte(IS)
for j in range(1,len(IS)):
    key=IS[j]
    print("Chave: %d"%(key))
    print("Estado Atual: ",end="")
    for p in IS:
        print("%d"%(p),end="")
        if p!=IS[len(IS)-1]:
            print(" | ",end="")
        else:
            print("")
    i=j-1
    while i>=0 and IS[i]>key:
        IS[i+1]=IS[i]
        i=i-1
        IS[i+1]=key
        for p in IS:
            print("%d"%(p),end="")
            if p!=IS[len(IS)-1]:
                print(" | ",end="")
            else:
                print("")
    print("")
print("Resultado Final: ",end="")
for p in IS:
    print("%d"%(p),end="")
    if p!=IS[len(IS)-1]:
        print(" | ",end="")
    else:
        print("")
   

