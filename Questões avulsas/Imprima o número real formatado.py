n=str(input())
i=0
while n[i]!=".":
    i+=1
if (len(n)-1)-i<6:
    for j in range((len(n)-1)-i,6):
        n=n+"0"
print("|%s.%s|"%(n[:i],n[i+1:i+3]))
print("|%s.%s|"%(n[:i],n[i+1:i+6]))
print("|      %s.%s|"%(n[:i],n[i+1:i+2]))
print("|%s.%s      |"%(n[:i],n[i+1:i+2]))
