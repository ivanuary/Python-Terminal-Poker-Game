import random
import os
# Classes
class Deck:
    def __init__(self, suit, rank, point):
        self.suit = suit
        self.rank = rank
        self.point = point

class Player:
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2

# Functions
def ifNotSameCard(card1:object, card2:object):
    if card1.suit == card2.suit and card1.rank == card2.rank:
        return 0
    else:
        return 1

def ifNotUsedCard(card1:object, used_cards:list):
    if len(used_cards) == 0:
        used_cards.append(card1)
        return 1
    else:
        for card in used_cards:
            if card1.suit == card.suit and card1.rank == card.rank:
                return 0
            else:
                used_cards.append(card1)
                return 1

# Card Deck
card_deck = []

ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = ['♠', '♥', '♦', '♣']
points = [1,2,3,4,5,6,7,8,9,10,11,12,13]

for suit in suits:
    for i, rank in enumerate(ranks, 1):
        card_input = Deck(suit, rank, i)
        card_deck.append(card_input)

# Used cards and Players
player_amount = 2
used_cards = []
players = []

# Card Picking for p1
for i in range(player_amount): 
    while True:
        card1 = random.choice(card_deck)
        card2 = random.choice(card_deck)
        same_card = ifNotSameCard(card1, card2)
        if same_card == 1:
            print("Valid")
            same_used_card = ifNotUsedCard(card1, used_cards)
            same_used_card2 = ifNotUsedCard(card2, used_cards)
            if same_used_card == 1 and same_used_card2 == 1:
                player_cards = Player(card1, card2)
                players.append(player_cards)
                print("Not Same Card")
                break



    


    


    

