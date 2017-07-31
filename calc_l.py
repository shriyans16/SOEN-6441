from decimal import *


class MathClass(object):
    @staticmethod
    def factorial(n):  # global variable to be used throughtout the program
        if n < 1:
            return 1
        else:
            return n * MathClass.factorial(n - 1)

    @staticmethod
    def calc_pi():
        p = Decimal(0)
        for a in xrange(0, 10):
            p += (Decimal(1) / (16 ** a)) * (
                (Decimal(4) / (8 * a + 1)) - (Decimal(2) / (8 * a + 4)) - (Decimal(1) / (8 * a + 5)) - (
                    Decimal(1) / (8 * a + 6)))  # BBPformula
        return float(p)

    @staticmethod
    def degree_to_radian(degree):
        return degree * 0.0174533

    @staticmethod
    def sin(x):  # function for calculating sin value
        sin_value = 0.0
        for n in range(0, 10):
            term1 = pow(-1, n)  # taylor series for calculating sine
            two_n_plus_one = (2 * n) + 1
            term2 = pow(x, two_n_plus_one)
            term3 = MathClass.factorial(two_n_plus_one)
            term12 = term1 * term2
            term123 = term12 / term3
            sin_value = sin_value + term123
        return sin_value

    @staticmethod
    def cos(x): # function for calculating cosine value
        cos_value = 0.0
        for n in range(0, 10):
            term1 = pow(-1, n)  # taylor series cos
            two_n = (2 * n)
            term2 = pow(x, two_n)
            term3 = MathClass.factorial(two_n)
            term12 = term1 * term2
            term123 = term12 / term3
            cos_value = cos_value + term123
        return cos_value
