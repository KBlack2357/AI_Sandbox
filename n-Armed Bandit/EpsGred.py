################################################################################
# The N-Armed Bandit Problem solved using the Epsilon-Greedy algorithm
# this program will test a range of epsilon values and output results
# call from terminal using "python EpsGred.py n nPlays epsLow epsHigh"
# i.e. "python EpsGred.py 14 2000 0.2 .22"
# n = number of different slot machines available to play
# nPlays = number of plays to simulate
# epsLow = lower limit for epsilon range
# epsHigh = upper limit for epsilon range
################################################################################
import numpy as np
from scipy import stats
import random
import matplotlib.pyplot as plt
from sys import argv
from sys import exit

script, n, nPlays, epsLow, epsHigh = argv # parameters included in program call
# convert input strings to required date types
n = int(n)
nPlays = int(nPlays)
epsLow = float(epsLow)
epsHigh = float(epsHigh)

# create epsilon range from the specified high and low boundaries
epsRange = np.arange(epsLow, epsHigh, 0.10)
if len(epsRange)>5: # don't allow more than 5 epsilon values
    print "eps range is too large"
    sys.exit()

epsLabels = [0 for j in range(len(epsRange))] # labels for each epsilon value for the plot
for i in range(len(epsLabels)):
    epsLabels[i] = "eps = %r" %format(epsRange[i], '.2f')

# specify colors for the plot
colors = [ 'r', 'b', 'g', 'k', 'm']

arms = np.random.rand(n) # stores the reward probabilities for each arm
rewardArray = np.array([0 for j in range(len(epsRange))]) # stores the rewards for each epsilon value
countArray = np.array([[0 for j in range(n)] for i in range(len(epsRange))]) # stores the number of times each arm is played per epsilon value

# reward function
def reward(prob):
    total = 0
    for i in range(10):
        if random.random() < prob:
            total += 1
    return total

# Function for returning the best arm.... Greedy part of Epsilon-Greedy Algorithm
def bestArm(a):
    return np.argmax(a) # returns index of element with greatest value

plt.xlabel("Plays")
plt.ylabel("Mean Reward")

for w in range(len(epsRange)):
    totalReward = 0
    runningMean = 0
    av = np.ones(n) # initialize action-value array
    counts = np.zeros(n) # stores counts of how many times we've taken a particular action
    eps = epsRange[w]

    for i in range(nPlays):
        if random.random() > eps: # Greedy action
            choice = bestArm(av)
            counts[choice] += 1
            k = counts[choice]
            rwd =  reward(arms[choice])
            old_avg = av[choice]
            new_avg = old_avg + (1/k)*(rwd - old_avg) # update running avg
            av[choice] = new_avg
        else: # Epsilon action
            choice = np.where(arms == np.random.choice(arms))[0][0] # randomly choose an arm (returns index)
            counts[choice] += 1
            k = counts[choice]
            rwd =  reward(arms[choice])
            old_avg = av[choice]
            new_avg = old_avg + (1/k)*(rwd - old_avg) # update running avg
            av[choice] = new_avg
        # have to use np.average and supply the weights to get a weighted average
        runningMean = np.average(av, weights=np.array([counts[j]/np.sum(counts) for j in range(len(counts))]))
        totalReward += rwd
        plt.scatter(i, runningMean, color= colors[w])
    plt.scatter(0, 0, label=epsLabels[w], color=colors[w]) # these points are only plotted for the plot legend.
    #If I specify a label within the "nPlays for loop" then each point is labeled on the legend. ### kind of a hack work around.
    countArray[w] = counts
    rewardArray[w] = totalReward
print "=" *50
print "Arms probabilities:"
print arms
print "=" *50
print "Total counts for each arm and eps value"
print countArray
print "total reward for each eps"
print rewardArray
print "\n"
print "=" *50

plt.legend(loc=4) #position the legend in bottom right corner of figure
plt.show()
