N=int(input())
Vec=[""]*N
V=input()
aux=""
V=V+" "
for i in range(len(V)):
    if V[i]!=" ":
        aux=aux+V[i]
    elif V[i]==" ":
        Vec.append(aux)
        aux=""
maior=0
for i in range(len(Vec)):
    if i==0:
        aux2=1
    elif Vec[i]==Vec[i-1]:
        aux2+=1
    else:
        maior=aux2
        aux2=1
    if aux2>maior:
        maior=aux2
print(maior)
