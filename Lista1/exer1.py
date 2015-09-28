N=input("Digite a quantidade de número a serem sorteados")
V=raw_input(":")
V=V.split(" ")
maior=0
teste=False
if len(V)<N:
    N=len(V)
    teste=True
for i in range(N):
    if i==0:
        aux=1
    elif V[i]==V[i-1]:
        aux+=1
    else:
        maior=aux
        aux=1
    if aux>maior:
        maior=aux
print maior
if teste:
    print "Você digitou menos números do que disse que faria"
elif len(V)>N:
    print "Você digitou mais números do que disse que faria"
