import pdb
from decimal import *


# getcontext().prec = 5

class MathClass(object):
    @staticmethod
    def factorial(n):  # global variable to be used throughtout the program
        if n < 1:
            return 1
        else:
            return n * MathClass.factorial(n - 1)


def calc_pi():
    p = Decimal(0)
    for a in xrange(0, 10):
        p += (Decimal(1) / (16 ** a)) * (
        (Decimal(4) / (8 * a + 1)) - (Decimal(2) / (8 * a + 4)) - (Decimal(1) / (8 * a + 5)) - (
        Decimal(1) / (8 * a + 6)))  # BBFformula
    return float(p)



def degree_to_radian(degree):
    return degree * 0.0174533


def compute_alpha():
    difference_value = 10
    alpha_value = 0.0
    pi_value = calc_pi()
    for degree in range(0, 360):
        radian = degree_to_radian(degree)
        sin_alpha = sin(radian)
        alpha_pi_by_two = radian - (pi_value / 2)
        current_diff = abs(sin_alpha - alpha_pi_by_two)
        if current_diff < difference_value:
            difference_value = current_diff
            alpha_value = radian
    return alpha_value


def sin(x):  # function for calculating sin value
    sineValue = 0.0
    for n in range(0, 10):
        term1 = pow(-1, n)  # taylor series for calculating sine and cos
        twoNplusOne = (2 * n) + 1
        term2 = pow(x, twoNplusOne)
        term3 = MathClass.factorial(twoNplusOne)
        term12 = term1 * term2
        term123 = term12 / term3
        sineValue = sineValue + term123
    return sineValue


def cos(x):
    cos_value = 0.0
    for n in range(0, 10):
        term1 = pow(-1, n)# taylor series
        twoN = (2 * n)
        term2 = pow(x, twoN)
        term3 = MathClass.factorial(twoN)
        term12 = term1 * term2
        term123 = term12 / term3
        cos_value = cos_value + term123
    return cos_value


alphaValue = compute_alpha()
print "Alpha Value : ", alphaValue
sinAlpha = sin(alphaValue)
cosAlphaByTwo = cos(alphaValue / 2)

print ("Calculating Length of Segment")
r = input("Enter radius : ")
term1 = (2 * r)
term2 = (1.0 - cosAlphaByTwo)
l_value = term1 * term2
print "Length of segment = ", l_value

f= open("output.txt","w")
f.write("Radius: " + str(r) +"\n"+ "Length of segment: "+ str(l_value))
f.close()
