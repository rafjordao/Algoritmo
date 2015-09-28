class No(object):
    def __init__(_self_,Key=None,Next=None):
        _self_.Key=Key
        _self_.Next=Next

class L(object):
    pass
    def __Init__(_self_,Nil=None):
        _self_.Nil=Nil

    def Insert(_self_,y):
        x=_self_.Nil.Next
        while x.Next!=None:
            x=x.Next
        x.Next=No(y)

    def Insert_Head(_self_,x):
        _self_.Nil.Next=No(x)


def Int(N):
    for i in range(len(N)):
        N[i]=int(N[i])

N=int(input())
for i in range(N):
    MC=str(input()).split()
    Int(MC)
    key=str(input()).split()
    Int(key)
    HashTable=[0]*MC[0]
    for k in range(MC[0]):
        HashTable[k]=L()
        HashTable[k].Nil=No()
    for j in key:
        Disper=j%MC[0]
        Nil=HashTable[Disper].Nil
        if Nil.Next!=None:
            HashTable[Disper].Insert(j)
        else:
            HashTable[Disper].Insert_Head(j)
    for k in range(MC[0]):
        print("%d ->"%(k),end="")
        x=HashTable[k].Nil
        while x.Next!=None:
            print(" %d ->"%(x.Next.Key),end="")
            x=x.Next
        print(" \\")
    print("")
                 
