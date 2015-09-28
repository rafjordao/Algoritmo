import math
def MinHeapify(N,i):
    global hs
    l=(2*i)+1
    r=(2*i)+2
    if l<=hs and N[l]<N[i]:
        shortest=l
    else:
        shortest=i
    if r<=hs and N[r]<N[shortest]:
        shortest=r
    if shortest!=i:
        N[i],N[shortest]=N[shortest],N[i]
        MinHeapify(N,shortest)
def BuildMinHeap(N,n):
    global hs
    hs=n-1
    for i in range(math.floor(n/2)-1,-1,-1):
        MinHeapify(N,i)
def HeapSort(N,n):
    global hs
    BuildMinHeap(N,n)
    for i in range(n-1,0,-1):
        N[0],N[i]=N[i],N[0]
        hs=hs-1
        MinHeapify(N,0)
    for i in range(n):
        if i!=(n-1):
            print("%d"%(N[i]),end=" ")
        else:
            print(N[i])
def invert(N,n):
    for i in range(n-1,-1,-1):
        N[i]=int(N[i])
        if i!=0:
            print("%d"%(N[i]),end=" ")
        else:
            print(N[i])
def UmPraEsquerda(N,n):
    for i in range(n):
        if i!=n-1:
            print("%d"%(N[i+1]),end=" ")
        else:
            print(N[0])
n=int(input())
N=str(input())
N=N.split()
invert(N,n)
UmPraEsquerda(N,n)
HeapSort(N,n)
