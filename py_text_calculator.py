# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:51:59 2019

@author: aschleper
"""

import math
from math import radians, sin, cos, tan

# Addition operation
a1 = float(input('Addition. Enter first number: '))
a2 = float(input('Enter second number: '))
a3 = a1 + a2
print(a1, '+', a2, '=', a3)

# Subtraction operation
s1 = float(input('Subtration: Enter first number: '))
s2 = float(input('Enter second number: '))
s3 = s1 - s2
print(s1, '-', s2, '=', s3)

# Multiplication operation
m1 = float(input('Multiplication: Enter first number: '))
m2 = float(input('Enter second number: '))
m3 = m1 * m2
print(m1, 'x', m2, '=', m3)

# Division operation
d1 = float(input('Division: Enter first number: '))
d2 = float(input('Enter second number: '))
d3 = d1 / d2
print(d1, '/', d2, '=', d3)

# Modulus operation
mo1 = float(input('Modulus: Enter first number: '))
mo2 = float(input('Enter second number: '))
mo3 = mo1 % mo2
print(mo1, '%', mo2, '=', mo3)

# Square root operation
sr1 = float(input('Square root: Enter number to take square root of: ')) 
sr2 = math.sqrt(sr1)
print('√', sr1, '=', sr2)

# Exponentiation operation
e1 = float(input('Exponentiation: Enter base number: '))
e2 = float(input('Enter power: '))
e3 = e1 ** e2
print(e1, '^', e2, '=', e3)

# sin, cos, and tan operations
angle = float(input('Enter number to compute sin, cos, and tan of: '))

# Calculate degrees
sine_degs = sin(radians(angle))
cosine_degs= cos(radians(angle))
tangent_degs = tan(radians(angle))

# Calculate radians
sine_rads = sin(angle)
cosine_rads = cos(angle)
tangent_rads = tan(angle)

print(sine_degs, '° sine')
print(sine_rads, 'r sine')
print(cosine_degs, '° cosine')
print(cosine_rads, 'r cosine')
print(tangent_degs, '° tangent')
print(tangent_rads, 'r tangent')

# Logarithm operation
lg1 = float(input('Logarithm: Enter value of x: '))
lg2 = float(input('Enter base: '))
lg3 = math.log(lg1, lg2)
print('log base', lg1, 'of', lg2, '=', lg3)