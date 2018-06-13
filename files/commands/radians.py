

def join(str):
    newstr = ''
    for i in str:
        newstr += i
    return newstr

def radians(expr):
    it = 0
    expr = list(expr)
    while True:

        for i in range(it, len(expr)):
            if expr[i] == 'c' or expr[i] == 's':
                expr.insert(i + 4, 'rad(')
                expr.insert(expr.index(')', i + 6), ')')
                it = i+6
                break
            else:
                it = len(expr)
        if it == len(expr):
            break
    return join(expr)

