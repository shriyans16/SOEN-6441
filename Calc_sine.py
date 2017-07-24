
def factorial(n):
    if n<1:
        return 1
    else:
        return n * factorial(n-1)

def sin(x):
    sineValue = 0.0
    term123 = 0.0
    for n in range(0,20):
        term1 = pow(-1, n)
        twoNplusOne = (2*n)+1
        term2 = pow(x, twoNplusOne)
        term3 = factorial(twoNplusOne)
        term12 = term1 * term2
        term123 = term12 / term3
        sineValue = sineValue + term123
        print "Nth value (", n, ") = ", sineValue
        pass

def cos(x):
        cosValue = 0.0
        term123 = 0.0
        for n in range(0, 20):
            term1 = pow(-1, n)
            twoN = (2 * n)
            term2 = pow(x, twoN)
            term3 = factorial(twoN)
            term12 = term1 * term2
            term123 = term12 / term3
            cosValue = cosValue + term123
            print "Nth value (", n, ") = ", cosValue
            pass




sin(2.303)
cos(1.159)


