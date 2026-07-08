import matplotlib.pyplot as plt
import numpy as np

colors = {"red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "gray", "cyan", "magenta"}
x = np.array([0,2,2,3,4,5,1,1,3,2,5])
y = np.array([0,2,5,3,4,5,2,1,5,4,1])
plt.subplot(2,2,1)
plt.scatter(x,y, c=colors)

x1 = np.array([0,2,2,3,4,5])
y1 = np.array([0,2,5,3,4,5])
plt.subplot(2,2,2)
plt.scatter(x1,y1, c="r")
x2 = np.array([1,1,3,2,5])
y2 = np.array([2,1,5,4,1])
plt.subplot(2,2,2)
plt.scatter(x2,y2, c="b")

x = np.array([0,2,2,3,4,5,1,1,3,2,5])
y = np.array([0,2,5,3,4,5,2,1,5,4,1])
plt.subplot(2,2,3)
plt.scatter(x,y, c=colors, cmap="viridis", s=100, alpha=0.5, edgecolors="k", linewidths=1)
plt.colorbar()

sizes = np.array([20, 50, 80, 200, 500, 1000, 60, 90, 10, 300, 600])
x = np.array([0,2,2,3,4,5,1,1,3,2,5])
y = np.array([0,2,5,3,4,5,2,1,5,4,1])
plt.subplot(2,2,4)
plt.scatter(x,y, c=colors, cmap="viridis", s=sizes, alpha=0.5, edgecolors="k", linewidths=1)
plt.colorbar()

plt.suptitle("Scatter Plot")

plt.show()