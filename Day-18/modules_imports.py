# Program 1 (Import math module)

import math

print(f"Square root of 25: {math.sqrt(25)}")
print(f"Value of pi: {math.pi}")


# Program 2 (Use more math functions)

import math

print(f"Ceiling of 4.2: {math.ceil(4.2)}")
print(f"Floor of 4.8: {math.floor(4.8)}")
print(f"Power 2^3: {math.pow(2, 3)}")


# Program 3 (Import specific things from math)

from math import sqrt, pi

print(f"Square root of 49: {sqrt(49)}")
print(f"Value of pi: {pi}")


# Program 5 (Import from custom module)

from my_utils import greet, square

print(greet("Pratham"))
print(f"Square of 6: {square(6)}")


# Program 6 (Use more functions from custom module)

from my_utils import add, make_upper

print(f"Sum: {add(10, 20)}")
print(f"Uppercase: {make_upper('pratham')}")


# Program 7 (Custom Module Practice)

from my_utils import greet, square
from my_utils import add, make_upper

name = "Pratham"

print(greet(name))
print(f"Square of 9: {square(9)}")
print(f"Sum of 12 and 8: {add(12, 8)}")
print(f"Uppercase name: {make_upper(name)}")