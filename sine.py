from decimal import *
getcontext().prec = 25
def factorial(n):
    if n<1:
        return 1
    else:
        return n * factorial(n-1)

def calc_sin(n):
    a=0.0001
    n=n*(3.142/180.0)
    x=n
    i=1
    while a < n:
        d= 2 * i * (2 * i + 1)
        x=-x * n * n / d
        x=n
        i = i + 1
        return n

for f in range(1,10):
    print "Iteration number", f, "",calc_sin(132)


