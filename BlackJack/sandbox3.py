import math
import random
print "\n" * 6



cardDict = {
    1 : 'Ace',
    2 : 2,
    3 : 3,
    4 : 4,
    5 : 5,
    6 : 6,
    7 : 7,
    8 : 8,
    9 : 9,
    10 : 10,
    11 : 'Jack',
    12 : 'Queen',
    13 : 'King'
}

card = random.randint(1,13)
print card
print "dealt a", cardDict[card]
