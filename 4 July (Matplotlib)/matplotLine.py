import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0,1,2,3,4,5,6])
y1 = np.array([3,4,3,2,3,4,3])
x2 = np.array([0,1,2,3,4,5,6])
y2 = np.array([3,2,3,4,3,2,3])
font1 = {"family":"serif", "color":"blue", "size":20}
plt.plot(x1, y1, "H-r", ms= 20, mec= "k", mfc= "b")  #"---" :- marker|lineStyle|color  ; mec = marker edge color  ; mfc = marker fill color
plt.plot(x2, y2, "H-b", ms= 20, mec= "k", mfc= "b")  #"---" :- marker|lineStyle|color  ; mec = marker edge color  ; mfc = marker fill color
plt.title("Matplot Line", fontdict= font1, loc="left")
#plt.grid()
#plt.grid(axis="x")
#plt.grid(axis="y")
plt.grid(axis="both")
plt.grid(color= "green", ls= ":", linewidth= 1.5)
plt.show()
