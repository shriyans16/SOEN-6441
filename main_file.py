from calc_l import *
from math import *
import xml.etree.cElementTree as ET


class Error(Exception):
    pass
class ValueSmallError(Error):
   pass
class ValueLargeError(Error):
   pass

def compute_alpha():
    difference_value = 10
    alpha_value = 0.0
    pi_value = MathClass.calc_pi()
    for degree in range(0, 360):
        radian = MathClass.degree_to_radian(degree)
        sin_alpha = MathClass.sin(radian)
        alpha_pi_by_two = radian - (pi_value / 2)
        current_diff = abs(sin_alpha - alpha_pi_by_two)
        if current_diff < difference_value:
            difference_value = current_diff
            alpha_value = radian
    return alpha_value


def calc_length():
    alpha_value = compute_alpha()
    print "Alpha Value : ", alpha_value
    cos_alpha_by_two = cos(alpha_value / 2)
    term1 = (2 * r)
    term2 = (1.0 - cos_alpha_by_two)
    l_value = term1 * term2
    return l_value

print ("Calculating Length of Segment")
while True:
    try:
        r = input("Enter radius : ")
        if r > 30:
            raise ValueLargeError
        elif r < 0:
            raise ValueSmallError
        break
    except ValueSmallError:
            print("Value should not be smaller")

    except ValueLargeError:
            print("Value cannot be greater")

length = calc_length()
print "Length : ", length


root = ET.Element("root")
doc = ET.SubElement(root, "doc")
ET.SubElement(doc, "field1", name="Value").text =str(r)
ET.SubElement(doc, "field2", name="Length").text = str(length)

tree = ET.ElementTree(root)
tree.write("Output.xml")
