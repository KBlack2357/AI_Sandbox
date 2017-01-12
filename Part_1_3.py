#imports
import numpy as np
from scipy import stats
import random
import matplotlib.pyplot as plt

n = 10
arms = np.random.rand(n)

av = np.ones(n)
counts = np.zeros(n)
av_softmax = np.zeros(n)
av_softmax[:] = 0.1 #initialize each action to have equal probability

def reward(prob):
    total = 0
    for i in range(10):
        if random.random() < prob:
            total += 1
    return total

tau = 1.12 #tau was selected by trial and error

def softmax(a):
    probs = np.zeros(n)
    for j in range(n):
        softm = (np.exp(av[j] / tau) / np.sum(np.exp(av[:] / tau)))
        probs[j] = softm
    return probs

totalReward = 0

plt.xlabel("Plays")
plt.ylabel("Mean Reward")

for i in range(1000):
    #select random arm using weighted probability distribution
    choice = np.where(arms == np.random.choice(arms, p=av_softmax))[0][0]
    counts[choice] += 1
    k = counts[choice]
    rwd = reward(arms[choice])
    old_avg = av[choice]
    new_avg = old_avg + (1/k)*(rwd - old_avg)
    av[choice] = new_avg
    av_softmax = softmax(av) #update softmax probabilities for the next play

    runningMean = np.average(av, weights=np.array([counts[j]/np.sum(counts) for j in range(len(counts))]))
    totalReward += rwd
    plt.scatter(i, runningMean)

print "\n"
print "Arms : "
print arms
print "counts :"
print counts
print "Total Reward : %r" %totalReward
print "\n \n"
plt.show()
