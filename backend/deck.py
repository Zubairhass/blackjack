import random

class Card(object):
    dhj

class shuffledDeck(list):
    def __init__(self):
        cards = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
        suits = ['S','H', 'C', 'D']

        for card in cards:
            for suit in suits:
                self.append(f"{card}_{suit}")

        random.shuffle(self)

deck = shuffledDeck()
print(deck)
print(deck[0].split('_')[0])


suits = list(range(4))
print(suits)