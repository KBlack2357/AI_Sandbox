import math
import random
from sys import exit
#each value card has a 1 in 13 chance of being selected (we don't care about suits in black jack)
#cards (value): Ace (1), 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack(10), Queen(10), King(10)
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

def randomCard():
    card = random.randint(1,13)
    print "dealt a", cardDict[card]
    if card > 10:
        card = 10
    return card

#a hand is just a tuple e.g. (14, false), a total card value of 14 without an ace

#accepts a hand, if the Ace can be an 11 without busting the hand, it's useable
def useable_ace(hand):
    val, ace = hand
    return ((ace) and ((val + 10) <= 21))

def totalValue(hand):
    val, ace = hand
    if (useable_ace(hand)):
        return (val + 10)
    else:
        return val

def add_card(hand, card):
    val, ace = hand
    if (card == 1):
        ace = True
    ace = useable_ace((val + card, ace))
    return (val + card, ace)

#the dealer is first dealt a single card, this method finishes off his hand
def eval_dealer(dealer_hand):
    while (totalValue(dealer_hand) < 17):
        dealer_hand = add_card(dealer_hand, randomCard())
    return dealer_hand

#state: (player total, useable_ace), (dealer total, useable_ace), game status
#stay or hit => dec ==0 or 1
def play(state, dec):
    #evaluate
    player_hand = state[0] #val, usable ace
    dealer_hand = state[1]
    if dec == 0: #action = stay
        #evaluate game; dealer plays
        print "=" * 8, "Dealer", "=" * 8
        dealer_hand = eval_dealer(dealer_hand)
        print "Dealer's hand:", dealer_hand
        print "\n"
        player_tot = totalValue(player_hand)
        dealer_tot = totalValue(dealer_hand)
        status = 1
        if (dealer_tot > 21):
            status = 2 #player wins
        elif (dealer_tot == player_tot):
            status = 3 #draw
        elif (dealer_tot < player_tot):
            status = 2 #player wins
        else: #dealer_tot > player_tot
            status = 4 #player loses
    else: # dec == 1: #action = hit
        #if hit, add new card to player's hand
        print "=" * 8, "Player", "=" * 8
        player_hand = add_card(player_hand, randomCard())
        print "Player's hand:", player_hand
        print "\n"
        print "=" * 8, "Dealer", "=" * 8
        dealer_hand = eval_dealer(dealer_hand)
        print "Dealer's hand:", dealer_hand
        print "\n"
        player_tot = totalValue(player_hand)
        dealer_tot = totalValue(dealer_hand)
        status = 1
        if (player_tot == 21):
            if (totalValue(dealer_hand) == 21):
                status = 3 #draw
            else:
                status = 2 #player wins
        elif (player_tot > 21):
            status = 4 #player loses
        elif (dealer_tot > 21):
            status = 2 # player wins
        else: #play_tot < 21, game still in progress
            status = 1
    state = (player_hand, dealer_hand, status)
    stateEval(state)

#start a game of blackjack, returns a random initial state
def initDeal():
    print "*" * 50
    print "\n"
    print "New Hand"
    print "\n"
    status = 1 #1 = in progress, 2 = player won, 3 = draw, 4 = player loses
    print "=" * 5, "Player", "=" * 5
    player_hand = add_card((0, False), randomCard())
    player_hand = add_card(player_hand, randomCard())
    print "Player's hand:", player_hand
    print "\n"
    print "=" * 5, "Dealer", "=" * 5
    dealer_hand = add_card((0, False), randomCard())
    print "Dealer's hand:", dealer_hand
    print "\n"
    #evaluate if player wins from first hand
    if totalValue(player_hand) == 21:
        if totalValue(eval_dealer(dealer_hand)) != 21:
            status = 2 #player wins
        else:
            status = 3 #draw
    if totalValue(dealer_hand) == 21:
        status = 4 # player loses
    if totalValue(dealer_hand) > 21:
        status = 2 # player wins
    state = (player_hand, dealer_hand, status)
    stateEval(state)

def stateEval(state):
    player_hand, dealer_hand, status = state
    if status == 1:
        print "Hand in progress.... Hit or Stay?"
        print "Enter 0 for Stay"
        print "Enter 1 for Hit"
        Decision = int(raw_input("> "))
        if Decision == 0:
            print "Stay"
        else:
            print "Hit"
        print "\n"
        play(state, Decision)
    else:
        if status == 2:
            print "You won the hand!"
        elif status == 3:
            print "This hand was a draw."
        else:
            print "You lost this hand."
    print "Do you want to play another hand? Enter Y or N"
    Decision = raw_input("> ")
    if Decision == "N":
        exit()
    initDeal()

initDeal()
