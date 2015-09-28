sequencia=str(input())
sequencia=sequencia.split()
X=sequencia[9]
cont=0
for i in sequencia:
    if X==i:
        cont+=1
X=int(X)
print("O numero %d apareceu %d vezes"%(X,cont))
