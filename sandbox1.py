#imports
import numpy as np
from scipy import stats
import random
import matplotlib.pyplot as plt

x = np.arange(0, 25, .1)
#print "x : %r" %x
sinx = np.sin(x)
cosx = np.cos(x)

plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,sinx, label="Sin(x)")
plt.plot(x,cosx, label="Cos(x)")
plt.legend()
plt.show()
