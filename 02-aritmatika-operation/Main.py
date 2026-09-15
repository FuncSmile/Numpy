import os
os.system('cls')
import numpy as np # type: ignore[import-not-found]


# list python
a = [1,2,3,4,5]
b = [6,7,8,9,10]

# array numpy
anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])

# ELEMENTWISE operation
# Addition
hasil = anp + bnp
print(F"Addition:\n{hasil}\n")
# Subtraction
hasil = anp - bnp
print(F"Subtraction:\n{hasil}\n")
# Multiplication
hasil = anp * bnp
print(F"Multiplication:\n{hasil}\n")

# Distribution
hasil = anp / bnp
print(F"Distribution:\n{hasil}\n")

# Squared Root
hasil = anp**2
print(F"squared root:\n{hasil}\n")

# Multiple array  numpy

c = np.array(([1,2,3],[4,5,6]))
d = np.array(([7,8,9],[-1,-2,-3]))

hasil = c + d
hasil = c * d
print(hasil)
