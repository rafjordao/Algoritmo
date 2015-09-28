def converte(N):
    for i in range(len(N)):
        N[i]=int(N[i])

def Insert(X):
    global Nil
    x=Clientes(X[0],X[1])
    x.Prev=Nil.Prev
    Nil.Prev.Next=x
    Nil.Prev=x
    x.Next=Nil

def menor(x):
    y=0
    for i in range(1,len(x)):
        if x[y].F_Op>x[i].F_Op:
            y=i
    return y

def Atendimento(T,D):
    global caixas
    if len(caixas)>1:
        y=menor(caixas)
    else:
        y=0
    if T<=caixas[y].F_Op:
        aux=caixas[y].F_Op
    else:
        aux=T
    caixas[y].F_Op=aux+D
    if aux - T>20:
        return True
    else:
        return False
    
class Caixa(object):
    def __init__(_self_,F_Op=0):
        _self_.F_Op=F_Op

CN=str(input())
CN=CN.split()
converte(CN)
caixas=[0]*CN[0]
maior_v=0
for i in range(CN[0]):
    caixas[i]=Caixa()
for i in range(CN[1]):
    cliente=str(input())
    cliente=cliente.split()
    converte(cliente)
    y=Atendimento(cliente[0],cliente[1])
    if y:
        maior_v+=1
print(maior_v)
