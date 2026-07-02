import numpy as np

z = np.array([1,2,5])
z = z[:, np.newaxis]
print(z)

y = np.array([[1,2,5],[2,4,4]])
y = y[np.newaxis, :]
print(y)