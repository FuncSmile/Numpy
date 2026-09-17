import os
os.system('cls')
import numpy as np # type: ignore[import-not-found]

# INDEXING - accessing a single element by its position

# indexing on 1-D array
arr1d = np.array([10, 20, 30, 40, 50])
print(F"first element (index 0): {arr1d[0]}")
print(F"last element (index -1): {arr1d[-1]}")
print(F"third element (index 2): {arr1d[2]}")

# indexing on 2-D array, format: [row, column]
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
print(F"row 0, col 0: {arr2d[0, 0]}")
print(F"row 1, col 2: {arr2d[1, 2]}")
print(F"last row, last col: {arr2d[-1, -1]}")

# indexing can also be used to change a value
arr2d[0, 0] = 100
print(F"arr2d after arr2d[0,0] is changed to 100: \n{arr2d}")

# indexing on 3-D array, format: [block, row, column]
arr3d = np.array([[[1, 2], [3, 4]],
                  [[5, 6], [7, 8]]])
print(F"block 0, row 1, col 0: {arr3d[0, 1, 0]}")
