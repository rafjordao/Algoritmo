import sys
try:
    for line in sys.stdin:
        if not line:
            sys.exit()
        maior=sequen=1
        p=line.split()
        x=int(p[0])
        y=int(p[1])
        aux=x
        if x>y:
            x=y
            y=aux
        while x<=y:
            i=x
            while i!=1:
                if i%2==1:
                    i=(i*3+1)
                    i>>=1
                    sequen+=2
                else:
                    i>>=1
                    sequen+=1
            if sequen>maior:
                maior=sequen
            sequen=1
            x+=1
        print("%s %s %d"%(p[0],p[1],maior))
except(KeyboardInterrupt, SystemExit, IndexError):
    sys.exit()
