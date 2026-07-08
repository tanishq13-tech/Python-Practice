import matplotlib.pyplot as plt
import numpy as np

font = {"color":'green', "size":10, "family":'timesNewRoman'}

x = np.array([0,1,2,3,4,5])
y = np.array([0,1,2,3,4,5])
plt.subplot(2,3,1)
plt.title("Linear Graph", fontdict=font)
plt.plot(x, y, c="r")

x = np.array([0,2,2,3,4,5])
y = np.array([0,2,5,3,4,5])
plt.subplot(2,3,3)
plt.title("Non-Linear Graph", fontdict=font)
plt.plot(x, y, c="r")

x = np.array([0,1,2,3,4,5])
y = np.array([3,3,3,3,3,3])
plt.subplot(2,3,5)
plt.title("Constant Graph", fontdict=font)
plt.plot(x, y, c="r")

plt.suptitle("Types of Graphs", c="k", family="TimesNewRoman", size=15)
plt.show()