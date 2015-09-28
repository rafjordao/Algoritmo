#try:
result=int(input())
n2=int(input())
sinal=str(input())
while sinal!="&":
    if sinal=="+":
        result=result+n2
        print("%.3f"%(result))
    elif sinal=="-":
        result=result-n2
        print("%.3f"%(result))
    elif sinal=="*":
        result=result*n2
        print("%.3f"%(result))
    elif sinal=="/" and (n2!=0 and result!=0):
        result=result/n2
        print("%.3f"%(result))
    else:
        print("operacao nao pode ser realizada")
    n2=int(input())
    sinal=str(input())
#except ZeroDivisionError:
#    print("operacao nao pode ser realizada")
