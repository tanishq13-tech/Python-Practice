import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,1,2,3,4,5,6])
y = np.array([3,4,3,2,3,4,3])
plt.subplot(1,2,1)
plt.plot(x,y)

x = np.array([0,1,2,3,4,5,6])
y = np.array([3,2,3,4,3,2,3])
plt.subplot(1,2,2)
plt.plot(x,y)

plt.show()
