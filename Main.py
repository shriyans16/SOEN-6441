from calc_l import *
import pdb

def compute_alpha():
        difference_value = 10
        alpha_value = 0.0
        pi_value = MathClass.calc_pi()                              #math class called from calc_l file
        for degree in range(0, 360):
            radian = MathClass.degree_to_radian(degree)          #conversion function called from calc_l file
            sin_alpha = MathClass.sin(radian)                      #sin function called from calc_l file
            alpha_pi_by_two = radian - (pi_value / 2)
            current_diff = abs(sin_alpha - alpha_pi_by_two)
            if current_diff < difference_value:
                difference_value = current_diff
                alpha_value = radian
        return alpha_value
pdb.set_trace()                                                   #inclusion of the use of debugger

def calc_length():
    alpha_value = compute_alpha()
    print "Alpha Value : ", alpha_value
    cos_alpha_by_two = MathClass.cos(alpha_value / 2)
    term1 = (2.0 * float(r))
    term2 = (1.0 - cos_alpha_by_two)
    l_value = term1 * term2
    return l_value
pdb.set_trace()
                                                  #inclusion of the use of debugger for verifying the correct output

alphaValue = compute_alpha()
print "Alpha Value : ", alphaValue
sinAlpha = MathClass.sin(alphaValue)
cosAlphaByTwo = MathClass.cos(alphaValue / 2)

print ("Calculating Length of Segment")
r = input("Enter radius : ")
term1 = (2.0 * float(r))
term2 = (1.0 - cosAlphaByTwo)
l_value = term1 * term2
print "Length of segment = ", l_value

f=open("Output.txt","w")                                        #output saved in text file
f.write("Radius: " + str(r) +"\n"+ "Length of segment: "+ str(l_value))
f.close()
