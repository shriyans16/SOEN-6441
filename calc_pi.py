from decimal import *
#getcontext().prec = 25

class Mathclass(object):
    @staticmethod
    def factorial(n):                                   #factorial to calculate for the formula
        if n<1:
            return 1
        else:
            return n * Mathclass.factorial(n-1)

    @staticmethod
    def calc_pi():                                      #calculating the pi value using the bpp formula
        p = Decimal(0)
        for a in xrange(0, 10):
            p += (Decimal(1) / (16 ** a)) * (
                (Decimal(4) / (8 * a + 1)) - (Decimal(2) / (8 * a + 4)) - (Decimal(1) / (8 * a + 5)) - (
                    Decimal(1) / (8 * a + 6)))                                      # BBPformula
        return float(p)