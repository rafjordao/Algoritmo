class NoG():
    def __init__(_self_,Key=None,KeyN=None):
        _self_.Key=Key
        _self_.Next=[]
        _self_.d=None
        _self_.pi={}

def Insert(N,x):
    aux=N.Next
    N.Next=No(x)
    N.Next.Next=aux

class No():
    def __init__(_self_,Key=None):
        _self_.Key=Key
        _self_.Next=None
        _self_.Prev=None
        

class G():
    def __init__(_self_,V):
        _self_.V=[None]*V
        _self_.Label={}
        for i in range(V):
            _self_.V[i]=NoG(i)

class Queue():
    def __init__(_self_):
        _self_.Nil=No()
        _self_.Nil.Next=_self_.Nil
        _self_.Nil.Prev=_self_.Nil
    def Enqueue(_self_,x):
        x=No(x)
        if _self_.Nil.Next==_self_.Nil:
            x.Prev=_self_.Nil
            x.Next=_self_.Nil
            _self_.Nil.Next=x
            _self_.Nil.Prev=x
        else:
            x.Prev=_self_.Nil.Prev
            x.Next=_self_.Nil
            _self_.Nil.Prev.Next=x
            _self_.Nil.Prev=x
    def Dequeue(_self_):
        x=_self_.Nil.Next
        _self_.Nil.Next=x.Next
        x.Next.Prev=_self_.Nil
        return x
    def is_empty(_self_):
        x=_self_.Nil.Next
        if x!=None and x!=_self_.Nil:
            return False
        else:
            return True
        

def BFS(G,Q,x):
    for i in G.V:
        i.d=-1
        i.pi=[]
    x.d=0
    x.pi=[]
    Q.Enqueue(x.Key)
    while not Q.is_empty():
        u=Q.Dequeue()
        u=G.V[G.Label[u.Key]]
        for j in G.V[G.Label[u.Key]].Next:
                j.visited=True
                j.d=u.d+1
                j.pi.append(u)
                Q.Enqueue(j.Key)
        
n=int(input())
index=0
grafo=G(n)
for i in range(n):
    Adj=str(input()).split()
    if not Adj[0] in grafo.Label:
        grafo.Label[Adj[0]]=index
        grafo.V[index].Key=Adj[0]
        index+=1
    for j in Adj[1:]:
        if not j in grafo.Label:
            grafo.Label[j]=index
            grafo.V[index].Key=j
            index+=1
        grafo.V[grafo.Label[Adj[0]]].Next.append(grafo.V[grafo.Label[j]])
coord=str(input()).split()
Fila=Queue()
BFS(grafo,Fila,grafo.V[grafo.Label[coord[0]]])
print(len(grafo.V[grafo.Label[coord[1]]].pi))
