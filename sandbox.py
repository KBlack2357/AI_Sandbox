#imports
import numpy as np
from scipy import stats
import random
import matplotlib.pyplot as plt
from sys import argv

script, xLow, xHigh, stepSize = argv
xLow = int(xLow)
xHigh = int(xHigh)
stepSize = float(stepSize)
print xLow, xHigh, stepSize, "\n"
x = np.arange(xLow, xHigh, stepSize)

sinx = np.sin(x)
cosx = np.cos(x)
#SinLabels = ["sin(x)", "2sin(x)", "3sin(x)", "4sin(x)", "5sin(x)"]

plt.xlabel("x")
plt.ylabel("y")


for i in range(1, 5):
    y = (i-1) *sinx
    plt.plot(x, y, label=i)

plt.legend()
plt.show()


"""x = np.arange(xLow, xHigh, stepSize)

sinx = np.sin(x)
cosx = np.cos(x)

plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,sinx, label="Sin(x)")
plt.plot(x,cosx, label="Cos(x)")
plt.legend()
plt.show()"""
