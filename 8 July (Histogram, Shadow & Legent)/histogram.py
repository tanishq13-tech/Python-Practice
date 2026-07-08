import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(20,2,2)
print(x)
print(len(x))
count = 0
dcount = 0
for i in range(len(x)):
    if x[i] < 20:
        count += 1
    else:
        dcount += 1
print(count)
print(dcount)
c = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'brown', 'gray', 'cyan']
plt.hist(x,  edgecolor='black', alpha=0.7, bins=10, histtype='stepfilled', linewidth=1.5, linestyle='--', hatch='X', label='Histogram')
plt.show()