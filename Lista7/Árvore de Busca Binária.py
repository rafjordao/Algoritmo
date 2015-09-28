class Stack():
    def __init__(self,x):
        self.itens=[""]*x
        self.top=-1

    def push(self,x):
        self.top+=1
        self.itens[self.top]=x

    def is_empty(self):
        if self.top==-1:
            return True
        return False

    def pop(self):
        if not self.is_empty():
            self.top-=1
            return self.itens[self.top+1]
        return False
    
    def peek(self):
        if not self.is_empty():
            return self.itens[self.top]

class No(object):
    def __init__(_self_,Key=None,P=None,R=None,L=None):
        _self_.Key=Key
        _self_.R=R
        _self_.L=L
        _self_.P=P

class Tree():
    def __init__(_self_,Root=None):
        _self_.Root=Root
        _self_.Ord=[]

    def enOrder(_self_,N):
        if N!=None:
            _self_.enOrder(N.L)
            _self_.Ord.append(N.Key)
            _self_.enOrder(N.R)
        
       
def Catch_Key(S,x):
    x+=1
    while S[x]!="(" and S[x]!=")":
        x+=1
    return x

def Catch_Sons(S):
    Pilha=Stack(len(S))
    Sons=[]
    for i in range(len(S)):
        if S[i]=="(":
            Pilha.push(S[i])
            if Pilha.top==0:
                Sons.append(i)
        elif S[i]==")":
            Pilha.pop()
    return Sons

def Create_Tree(S,N,LR):
    x=Catch_Key(S,LR[0])
    if S[LR[0]+1:x]!="":
        N.L=No(int(S[LR[0]+1:x]),N)
        LS=Catch_Sons(S[x:LR[1]])
        Create_Tree(S[x:LR[1]],N.L,LS)
    y=Catch_Key(S,LR[1])
    if S[LR[1]+1:y]!="":
        N.R=No(int(S[LR[1]+1:y]),N)
        RS=Catch_Sons(S[y:len(S)-1])
        Create_Tree(S[y:len(S)-1],N.R,RS)
            
S=str(input())
x=Catch_Key(S,0)
BT=Tree()
BT.Root=No(int(S[1:x]))
Sons=Catch_Sons(S[x:len(S)-1])
Create_Tree(S[x:len(S)-1],BT.Root,Sons)
BT.enOrder(BT.Root)
N=True
for i in range(len(BT.Ord)):
    if i<len(BT.Ord)-1 and BT.Ord[i]>BT.Ord[i+1]:
        N=False
if N:
    print("VERDADEIRO")
else:
    print("FALSO")
    
