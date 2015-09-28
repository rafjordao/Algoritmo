ponto=0
totalC=0
totalEDF=0
n=0
def gol():
    global n
    global totalC
    global totalEDF
    ponto=int(input())
    if n%2==0:
        totalC+=ponto
    else:
        totalEDF+=ponto
while n<10:
    gol()
    if n==5 and ((totalC-totalEDF==3)or(totalEDF-totalC==3)):
        n+=5
    elif n==7 and ((totalC-totalEDF>=2)or(totalEDF-totalC>=2)):
        n+=3
    n+=1
while totalC==totalEDF:
    gol()
    n+=1
    gol()
    n+=1
if totalC>totalEDF:
    print("COMPUTACAO.RAR")
else:
    print("EDUCACAO FISICA")
    
