import numpy as np

a = np.array([1,1,0,0], dtype=bool)
b = np.array([1,0,0,0], dtype=bool)
print(np.logical_or(a,b))
print(np.logical_and(a,b))
print(np.logical_not(a))