import numpy as np

a = np.array([1,2,3,4])
b = np.array([1,2,4,4])
c = np.array([1,2,4,4])
print(np.array_equal(a,b))
print(np.array_equal(b,c))