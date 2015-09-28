c=b=0
for i in range(7):
    escolhas=str(input())
    if ((escolhas[0]=="c")or(escolhas[0]=="C")):
        c+=1
    else:
        b+=1
if c>b:
    print("CINEMA")
else:
    print("BOLICHE")
