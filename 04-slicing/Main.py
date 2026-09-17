import os
os.system('cls')
import numpy as np # type: ignore[import-not-found]

# SLICING - taking a range of elements [start:end:step]
# note: the 'end' index is not included in the result

a = np.arange(1, 11)
print(F"array a: {a}")

print(F"a[2:5]   -> index 2 to 4: {a[2:5]}")
print(F"a[:4]    -> from the start to index 3: {a[:4]}")
print(F"a[5:]    -> from index 5 to the end: {a[5:]}")
print(F"a[::2]   -> every 2nd element: {a[::2]}")
print(F"a[1:8:2] -> index 1 to 7, step 2: {a[1:8:2]}")
print(F"a[::-1]  -> reversed array: {a[::-1]}")

# slicing on a 2-D array, format: [row, column]
m = np.array([[10, 20, 30, 40],
              [50, 60, 70, 80],
              [90, 100, 110, 120]])
print(F"matrix m: \n{m}")

print(F"m[0:2]      -> first two rows: \n{m[0:2]}")
print(F"m[:, 1]     -> column index 1 only: {m[:, 1]}")
print(F"m[1, 1:3]   -> row 1, column 1 to 2: {m[1, 1:3]}")
print(F"m[0:2,0:2]  -> top-left 2x2 sub-matrix: \n{m[0:2, 0:2]}")
print(F"m[:, ::2]   -> every 2nd column: \n{m[:, ::2]}")
