import math
def imprime(N,s1="Estado",s2="Atual"):
    print("%s %s:"%(s1,s2),end=" ")
    for i in range(len(N)):
        print("%d"%(N[i]),end="")
        if i!=len(N)-1:
            print(" | ",end="")
        else:
            print("\n")
def SelectionSort(N):
    for i in range(math.floor(len(N)/2)):
        menor=i
        maior=len(N)-1-i
        for j in range(i+1,len(N)-1-i):
            if N[j]<N[menor]:
                menor=j
            if N[j]>N[maior]:
                maior=j
        print("Menor elemento neste passo: %d"%(N[menor]))
        print("Maior elemento neste passo: %d"%(N[maior]))
        N[i],N[menor]=N[menor],N[i]
        N[len(N)-1-i],N[maior]=N[maior],N[len(N)-1-i]
        imprime(N)
def converte(N):
    for i in range(len(N)):
        N[i]=int(N[i])
N=str(input())
N=N.split()
converte(N)
SelectionSort(N)
imprime(N,"Resultado","Final")

