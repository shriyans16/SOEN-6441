import math
from calc_pi import *                                  #i
import xml.etree.cElementTree as ET

class Error(Exception):                             #exception handling class
   pass
class ValueSmallError(Error):
    pass
class ValueLargeError(Error):
  pass

def compute_alpha():
    difference_value = 10
    alpha_value = 0.0
    pi_value = Mathclass.calc_pi()                  #pi value is called from class that calculates pi by BPP formula
    for degree in range(0, 360):
        radian = math.radians(degree)
        sin_alpha = math.sin(radian)                #sin import from math function
        alpha_pi_by_two = radian - (pi_value / 2)
        current_diff = abs(sin_alpha - alpha_pi_by_two)
        if current_diff < difference_value:             #checking the value difference for computing alpha
            difference_value = current_diff
            alpha_value = radian
    return alpha_value


def calc_length():                                      #function to calculate the length of segment
    alpha_value = compute_alpha()
    print "Alpha Value : ", alpha_value
    cos_alpha_by_two = math.cos(alpha_value / 2)
    term1 = (2.0 * float(r))
    term2 = (1.0 - cos_alpha_by_two)
    l_value = term1 * term2
    return l_value


print ("Calculating Length of Segment")
while True:
     try:
        r = input("Enter radius : ")
        if r > 30:                                      #error message if radius input is greater than 30
            raise ValueLargeError
        elif r <= 0:                                     #error message if radius input is less than or equal to 0
          raise ValueSmallError
        break
     except ValueSmallError:
         print ("Value should not be negative or 0")
     except ValueLargeError:
         print("Value should not be greater than 30")

length = calc_length()
print "Length : ", length

root = ET.Element("root")                                       #xml basic root and element structure
doc = ET.SubElement(root, "doc")
ET.SubElement(doc, "field1", name="Radius").text =str(r)
ET.SubElement(doc, "field2", name="Length").text = str(length)
tree = ET.ElementTree(root)
tree.write("Output.xml")                                        #output saved in output.xml file format


