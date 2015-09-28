n=int(input())
while n!=0:
    L=[""]*n
    for i in range(n):
        L[i]=str(input())
    L.sort()
    for i in L:
        print(i)
    n=int(input())
        
