import numpy as np

# Flatening
x = np.array([[1,2],[3,4]])
print(x.ravel())

# Reshaping
x = np.array([[1,2],[3,4]])
b = x.ravel()
b = b.reshape((4,1))
print(b)

x = np.array([[1,2],[3,4]]).ravel().reshape((4,1))
print(x)
