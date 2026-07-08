import matplotlib.pyplot as plt
import numpy as np

x = np.array([20, 30, 40, 50, 60])
y = np.array(["apples", "bananas", "cherries", "dates", "elderberries"])
plt.pie(x, labels=y, explode=(0, 0.1, 0, 0, 0), shadow=True, startangle=90, autopct='%1.1f%%')
plt.legend(title="Fruits", loc="lower right", fontsize=10, title_fontsize=12, fancybox=True, shadow=True, edgecolor='black', bbox_to_anchor=(1.2, 0.1))
plt.show()

