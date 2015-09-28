H24=int(input())
M24=int(input())
hora="am"
if H24>=12:
    hora="pm"
H12=H24%12
if H12==0:
    H12=12
print("%02d"%(H12))
print("%02d"%(M24))
print(hora)
