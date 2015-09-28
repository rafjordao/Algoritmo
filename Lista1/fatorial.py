def fatorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fatorial(n-1)
N=int(input())
while N!=-1:
    print(fatorial(N))
    N=int(input())

