import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import RMSprop
def randPair(s,e):
    return np.random.randint(s,e), np.random.randint(s,e)

#find an array in the "depth" dimension of the grid
def findLoc(state, obj):
    for i in range(0, 4):
        for j in range(0, 4):
            if (state[i, j] == obj).all():
                return i, j

#initialize stationary grid, all items are placed deterministically
def initGrid():
    state = np.zeros((4,4,4))
    #place player
    state[0, 1] = np.array([0, 0, 0, 1])
    #place wall
    state[2, 2] = np.array([0, 0, 1, 0])
    #place pit
    state[1, 1] = np.array([0, 1, 0, 0])
    #place goal
    state[3, 3] = np.array([1, 0, 0, 0])

    return state

def getLoc(state, level): #used to check if player is suerimposed on goal or pit
    for i in range(0,4):
        for j in range(0,4):
            if (state[i,j][level] == 1):
                return i,j

def dispGrid(state):
    grid = np.zeros((4,4), dtype='<U2')
    player_loc = findLoc(state, np.array([0,0,0,1]))
    wall = findLoc(state, np.array([0,0,1,0]))
    goal = findLoc(state, np.array([1,0,0,0]))
    pit = findLoc(state, np.array([0,1,0,0]))
    for i in range(0,4):
        for j in range(0,4):
            grid[i,j] = ' '

    if player_loc:
        grid[player_loc] = 'P' #player
    if wall:
        grid[wall] = 'W' #wall
    if goal:
        grid[goal] = '+' #goal
    if pit:
        grid[pit] = '-' #pit

    return grid

state = initGrid()
#print state
print dispGrid(state)
print "\n"
state = makeMove(state, 3)
print dispGrid(state)
print "\n"
state = makeMove(state, 3)
print dispGrid(state)
print "\n"
state = makeMove(state, 1)
print dispGrid(state)
print "\n"
state = makeMove(state, 1)
print dispGrid(state)
print "\n"
print "Reward: %r" %(getReward(state))
state = makeMove(state, 1)
print dispGrid(state)
print "\n"
print "Reward: %r" %(getReward(state))
