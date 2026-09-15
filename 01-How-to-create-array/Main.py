import os
os.system('cls')
import numpy as np # type: ignore[import-not-found]

# create vector/array in numpy
a = np.array([1,2,3,4,5])
print(F"int vector/array in numpy: {a}")
b = np.array([1.1,1.2,1.3,2,3])
print(F"float vector/array in numpy: {b}")
# create vector use range
c = np.arange(1, 10, 1)
print(F"from 1 to 10 in multiples of 1 {c}")
#  create vector use linspace
d = np.linspace(1, 10, 4)
print(F"from 1 to 10 in multiples of 4-1 {d}")
# create matrix use numpy
e = np.array([ (1,2,3), (4,5,6) ])
print(F"Matrix: \n {e}")
# matrix use zero value
f = np.zeros(5)
print(F"zero values: {f}")
g = np.zeros((5, 5))
print(F"matrix zero values: \n {g}")
# matrix use one value
h = np.ones(5)
print(F"one values: {h}")
i = np.ones((5, 5))
print(F"matrix one values: \n {i}")
# matrix identity
j = np.identity(5)
print(F"matrix values: \n {j}")
j = np.eye(5)
print(F"matrix values: \n {j}")








