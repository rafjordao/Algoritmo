A=B=C=Zero=Um=0
def teste():
    result=int(input())
    return result
A=teste()
B=teste()
C=teste()
if A!=B and A!=C:
    print("A")
elif B!=A and B!=C:
    print("B")
elif C!=A and C!=B:
    print("C")
else:
    print("*")
