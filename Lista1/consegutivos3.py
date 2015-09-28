N=int(input())
V=str(input())
V=V.split()
aux2=maior=0
aux=V[0]
for i in V:
    if i==aux:
        aux2=aux2+1
    else:
        aux=i
        if aux2>maior:
            maior=aux2
        aux2=1
if aux2>maior:
    maior=aux2
print(maior)
