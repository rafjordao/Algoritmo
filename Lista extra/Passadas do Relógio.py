def converte(N):
    for i in range(len(N)):
        N[i]=int(N[i])

N=str(input())
N=N.split()
converte(N)
H1=N[0]%12
H1=(H1*60)+N[1]
H2=N[2]%12
H2=(H2*60)+N[3]
C1=H2//65
C2=H1//65
if ((N[0]%12)==(N[2]%12) and N[1]>N[3])or(N[0]%12)>(N[2]%12):
    CF=11+(C1-C2)
else:
    CF=C1-C2
print(CF)
