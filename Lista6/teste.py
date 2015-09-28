def rpn(s):
    var_list = []
    symb_list = []
    for c in s:
        if c in "abcdefghijylmnopqrstuvwxyz":
            var_list.append(c)
        elif c in ['^', '*', '/', '+', '-']:
            symb_list.append(c)
        elif c == ')':
            x = var_list.pop()
            y = var_list.pop()
            z = symb_list.pop()
            var_list.append(y + x + z)
        #print var_list, symb_list
        
    return var_list[0]
        
t = int(input())

while t:
    t -= 1
    s = input()        
    print(rpn(s))
