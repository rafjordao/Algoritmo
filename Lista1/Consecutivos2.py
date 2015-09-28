N=int(input())
V=str(input())
V=V.split()
maior=0
for i in range(len(V)):
    if i==0:
        aux2=1
    elif V[i]==V[i-1]:
        aux2+=1
    else:
        maior=aux2
        aux2=1
    if aux2>maior:
        maior=aux2
print(maior)
