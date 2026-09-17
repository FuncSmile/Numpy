import os
os.system('cls')
import numpy as np # type: ignore[import-not-found]

# ITERATION - looping through array elements

a = np.arange(1, 11)
print(F"array a: {a}")

m = np.array([[10, 20, 30, 40],
              [50, 60, 70, 80],
              [90, 100, 110, 120]])
print(F"matrix m: \n{m}")

# iterating a 1-D array returns each element directly
print("iterate array a:")
for x in a:
    print(x, end=" ")
print()

# iterating a 2-D array returns each row, not each element
print("iterate matrix m (per row):")
for row in m:
    print(row)

# a nested loop is needed to reach each element
print("iterate matrix m (per element):")
for row in m:
    for val in row:
        print(val, end=" ")
print()

# np.nditer() can loop through all elements of an N-D array directly
print("iterate matrix m using np.nditer:")
for x in np.nditer(m):
    print(x, end=" ")
print()

# np.nditer() with op_dtypes to change the data type while iterating (needs a buffer)
print("iterate array a as bytes:")
for x in np.nditer(a, flags=["buffered"], op_dtypes=["S"]):
    print(x, end=" ")
print()

# np.nditer() combined with slicing, to skip a column each step
print("iterate matrix m, every 2nd column:")
for x in np.nditer(m[:, ::2]):
    print(x, end=" ")
print()

# np.ndenumerate() gives the index and the value at the same time
print("iterate matrix m with its index:")
for idx, val in np.ndenumerate(m):
    print(idx, val)
