DicTrad = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
Decimal=0
Rom=str(input())
for i in range(len(Rom)):
    aux = DicTrad[Rom[i]]
    if i+1 < len(Rom) and DicTrad[Rom[i+1]] > aux:
        Decimal = Decimal - aux
    else:
        Decimal = Decimal + aux
res=Decimal%5
if res==0:
    print("O numero e multiplo de 5!")
else:
    print("O resto pela divisao por 5 do numero dado e igual a %d!"%(res))
