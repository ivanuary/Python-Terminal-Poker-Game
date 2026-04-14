import random

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
    verify = 0   
    if len(used_cards) == 0:
        used_cards.append(card1)
        verify = 1
    else:
        for i in range(len(used_cards)):
            if card1.suit == used_cards[i].suit and card1.rank == used_cards[i].rank:
                return 0
            else:
                verify = 1
        if verify == 1:
            used_cards.append(card1)

    return verify
# Start
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
river = []
used_cards = []
players = []

# Card Picking for p1
for i in range(player_amount): 
    while True:
        card1 = random.choice(card_deck)
        same_used_card = ifNotUsedCard(card1, used_cards)
        if same_used_card == 1:
            break
    
    while True:
        card2 = random.choice(card_deck)
        same_used_card2 = ifNotUsedCard(card2, used_cards)
        if same_used_card2 == 1:
            break
    
    player_cards = Player(card1, card2)
    players.append(player_cards)

for i in range(5):
    while True:
        river_card = random.choice(card_deck)
        used_card = ifNotUsedCard(river_card, used_cards)
        if used_card == 1:
            river.append(river_card)
            break

p1 = []
p2 = []


# Add Cards to a list to be checked later
p1.append(players[0].card1)
p1.append(players[0].card2)

p2.append(players[1].card1)
p2.append(players[1].card2)

for card in river:
    p1.append(card)
    p2.append(card)

while True:
    print("===================")
    print("The Table is: ")
    for card in river:
        print(f"{card.suit}{card.rank}", end=' ')
    print("\n\nPlayer 1 Has: ")
    print(f"{players[0].card1.suit}{players[0].card1.rank}  {players[0].card2.suit}{players[0].card2.rank}")
    break


    


