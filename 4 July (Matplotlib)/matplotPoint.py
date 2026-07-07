import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,6,9])
y = np.array([0,6,9])
font1 = {"family":"serif", "color":"blue", "size":20}
#plt.plot(x, y, "o")
plt.plot(x, y, "H", ms=20, mec= "k", mfc= "b")  #"---" :- marker|lineStyle|color  ; mec = marker edge color  ; mfc = marker fill color
plt.title("Matplot Point", fontdict= font1, loc="left")
plt.xlabel("Number of persons", fontdict=font1)
plt.ylabel("Number of chocolates", fontdict=font1)
plt.show()
