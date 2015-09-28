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
    
def Posfixacao(A):
    pre={}
    pre["^"]=5
    pre["*"]=4
    pre["/"]=3
    pre["+"]=1
    pre["-"]=1
    pre["("]=0
    pre[")"]=0
    S=""
    Op=Stack(len(A))
    waiting=False
    for i in range(len(A)):
        print(A[i])
        if A[i]!="(" and A[i]!=")" and A[i]!="+" and A[i]!="-" and A[i]!="*" and A[i]!="/" and A[i]!="^":
            S="%s%s"%(S,A[i])
        elif A[i]=="(":
            Op.push(A[i])
        elif A[i]==")":
            j=Op.pop()
            while j!="(":
                S="%s%s"%(S,j)
                j=Op.pop()
        else:
            k=i+1
            while not Op.is_empty() and pre[Op.peek()]>=pre[A[i]]:
                if pre[Op.peek()]==pre[A[i]]:
                    while k<len(A)-1 and (A[k]!="+" and A[k]!="-" and A[k]!="*" and A[k]!="/" and A[k]!="^"):
                        k+=1
                    if waiting:
                        S="%s%s"%(S,Op.pop())
                        waiting=False
                        break
                    elif A[k] not in "+-*/^" or pre[A[k]]>pre[A[i]]:
                        break
                    elif not waiting:
                        waiting=True
                        break                   
                S="%s%s"%(S,Op.pop())              
            Op.push(A[i])
        for j in range(Op.top+1):
            print(" %s |"%(Op.itens[j]),end=" ")
        print("|::| %s"%(S))
    while not Op.is_empty():
        i=Op.pop()
        S="%s%s"%(S,i)
    return S

N=int(input())
for i in range(N):
    infixa=str(input())
    posfixa=Posfixacao(infixa)
    print(posfixa)
