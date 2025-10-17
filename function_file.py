def leftpointrule(F,n,a,b):
    width = (b - a) / n
    sum = 0
    for i in range(0,n):
        sum += F[i]
    return sum * width

def midpointrule(F,n,a,b):
    sum = 0
    for i in range(1,n - 1):
        sum += F[i + 1] + F[i - 1]
    width = (b - a) / (2 * n)
    return sum * width

def trapizoidrule(F,n,a,b):
    width = (b - a) / n
    sum = (F[0] + F[n - 1]) / 2
    for i in range(1,n - 1):
        sum += F[i]
    return sum * width

def simpsonsrule(F,n,a,b):
    width = (b - a) / (3 * n)
    sum = (F[0] + F[n - 1])
    for i in range(1,n - 1,2):
        sum += 4 * F[i]
    for i in range(2,n - 2,2):
        sum += 2 * F[i]
    return sum * width

def optimal_integrator(F,n,a,b): #cant handle n lower than 4
    if n//2 == 0:
        return simpsonsrule(F,n,a,b)
    else:
        return trapizoidrule(F,n,a,b)
