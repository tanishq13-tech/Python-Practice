import matplotlib.pyplot as plt
import numpy as np

colors = {"red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "gray", "cyan", "magenta"}
x = np.array([0,2,2,3,4,5,1,1,3,2,5])
y = np.array([0,2,5,3,4,5,2,1,5,4,1])
plt.subplot(1,2,1)
plt.bar(x,y, color=colors, width=0.5, edgecolor="k", linewidth=1, alpha=0.7)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

x = np.array([0,2,2,3,4,5,1,1,3,2,5])
y = np.array([0,2,5,3,4,5,2,1,5,4,1])
plt.subplot(1,2,2)
plt.barh(x,y, color=colors, height=0.5, edgecolor="k", linewidth=1, alpha=0.7)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.suptitle("Bar Chart")
plt.show()