import numpy as np

a = np.array([1,3,2,4])
print(np.sort(a))

a = np.array([[1,3,2,4],[2,5,1,3]])
print(np.sort(a, axis=1))

a.sort(axis=0)
print(a)