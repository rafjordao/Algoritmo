class No():
    def __init__(_self_,Key=None,KeyN=None):
        _self_.Key=Key
        _self_.Next=None
        _self_.Adj=None
        _self_.index=0
        _self_.d=0
        _self_.visited=False
        _self_.pi=[]

def InsertNext(N,x):
    aux=N.Next
    N.Next=No(x)
    N.Next.Next=aux

def InsertAdj(N,x):
    aux=N.Adj
    n.Adj=No(x)
    N.Adj.Adj=aux

class G():
    def __init__(_self_):
        _self_.Label={}

       
def DFS_Visit(Gr,u,x):
    if u.Key==x.Key:
        u.d+=1
        Gr.V[u.index].d+=1
        return
    i=u
    while i!=None:
        if not i.visited:
            i.d+=1
            i.pi.append(u)
            Gr.V[i.index].=
            DFS_Visit(Gr,Gr.V[i.index],x)
        i=i.Next
        
f=open("caminhos.txt","r")
n=int(f.readline())
index=0
grafo=G(n)
for i in range(n):
    Adj=str(f.readline()).split()
    if not Adj[0] in grafo.Label:
        grafo.Label[Adj[0]]=No(Adj[0])
    for j in Adj[1:]:
        if not j in grafo.Label:
            grafo.Label[Adj[0]]=No(Adj[0])
        Insert(grafo.V[index-1],j)
coord=str(f.readline()).split()

DFS_Visit(grafo,grafo.V[grafo.Label[coord[0]]],grafo.V[grafo.Label[coord[1]]])
print(grafo.V[grafo.Label[coord[1]]].d)
