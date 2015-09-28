def converte(n):
    for i in range(len(n)):
        n[i]=n[i].split()
        for p in range(len(n[i])):
            n[i][p]=int(n[i][p])
    return n
X=[]
with open("3n +1.in","r") as entrada:
    for line in entrada:
        X.append(line)
X=converte(X)
cont=0
maior=sequen=0
while cont<(len(X)):
    for i in range(X[cont][0],X[cont][1]+1):
        n=i
        while n!=1:
            if n%2==0:
                n=n/2
            else:
                n=n*3+1
            sequen=sequen+1
        if sequen>maior:
            maior=sequen
            sequen=1
        else:
            sequen=1
    print("%d %d %d"%(X[cont][0],X[cont][1],maior))
    cont+=1
    maior=sequen=0
