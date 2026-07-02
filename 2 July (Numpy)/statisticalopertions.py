import numpy as np

x = np.array([1,2,3,1])
y = np.array([[1,2,3],[3,4,1]])
print(x.mean())
print(np.median(x))
print(y.mean(axis=1))
print(y.mean(axis=0))
print(np.median(y, axis=1))
print(np.median(y, axis=0))