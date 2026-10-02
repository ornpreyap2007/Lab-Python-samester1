import math as m
import numpy as np
import matplotlib.pyplot as plt

x1 = np.arange(-5,1,0.1)
y1 = 7-4*x1

x2 = np.arange(1,5,0.1)
y2 = x2**2+2

plt.plot(x1,y1, color="red",linewidth=1,linestyle="dotted")
plt.plot(x2,y2, color="blue",linewidth=1,linestyle="dotted")
plt.show()