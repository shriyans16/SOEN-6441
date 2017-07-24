from decimal import *
#getcontext().prec = 25

def factorial(n):
    if n<1:
        return 1
    else:
        return n * factorial(n-1)

def calc_pi(n):
    p = Decimal(0)
    a = 0
    while a < n:
        p += (Decimal(1)/(16**a))*((Decimal(4)/(8*a+1))-(Decimal(2)/(8*a+4))-(Decimal(1)/(8*a+5))-(Decimal(1)/(8*a+6)))
        a += 1
    return p


print "\t\t\t Pi Value "
for i in xrange(1,10):
    print "Iteration number ",i, " ", calc_pi(i)
