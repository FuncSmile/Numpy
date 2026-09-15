import numpy as np  # type: ignore[import-not-found]

a = np.array([1,2,3,4,5])
b = [1,2,3,4,5]

print(a)
print(b)
a = a + 1
# b = b + 1 akan error 
b = b + [1]
print(a)
print(b)