#imports
import numpy as np
from scipy import stats
import random
import matplotlib.pyplot as plt
#from sys import argv


w, h = 2, 5
resultsArray = ([[0 for x in range(w)] for y in range(h)])
print resultsArray
print resultsArray[1]
resultsArray[1] = [1, 2]
print resultsArray[1]
print resultsArray[1][0]
print resultsArray[1][1]
print resultsArray

resultsArray[1][0] = [1, 2, 3, 4]
print resultsArray[1]
print resultsArray[1][0]
print resultsArray[1][1]
print resultsArray


counts = np.zeros(10)
rewards = np.ones(5)
"""
for i in range(0, h-1):
    thisResult = np.array([[counts], rewards[i]])
    resultsArray[i] =
print resultsArray



SinLabels = ["sin(x)", "2sin(x)", "3sin(x)", "4sin(x)", "5sin(x)"]

plt.xlabel("x")
plt.ylabel("y")


for i in range(1, 5):
    y = (i-1) *sinx
    plt.plot(x, y, label=SinLabels[i-1])

plt.legend()
plt.show()


x = np.arange(xLow, xHigh, stepSize)

sinx = np.sin(x)
cosx = np.cos(x)

plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,sinx, label="Sin(x)")
plt.plot(x,cosx, label="Cos(x)")
plt.legend()
plt.show()"""
