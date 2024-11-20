import random
class Deck:
    def __init__(self):

        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.deck = []

        for suit in suits:
            for rank in ranks:
                card = f"{rank} of {suit}"
                self.deck.append(card)

    def pick(self):
        try:
            card = self.deck.pop(0)
            return card
        except IndexError:
            return None

    def pick_any(self):
        try:
            card = random.choice(self.deck)
            self.deck.remove(card)
            return card
        except IndexError:
            return None

    def shuffle(self):
        random.shuffle(self.deck)

print('generating new deck...')
print()

d = Deck()

print('picking card from deck 53 times...')
print()

for i in range(53):
    card = d.pick()
    print(card)

if card is not None:
    print('error:  .pick() must return the None value (not ' +
          "string 'None')")
    exit()

print()

print('generating a new deck...')

e = Deck()

print('picking first card from new deck...')
print()

ecard = e.pick()
print(ecard)
print(); print()

print('picking random card from new deck...')
print()

ecard = e.pick_any()
print(ecard)
print(); print()

print('shuffling...')
print()

e.shuffle()

print('picking first card from the shuffled deck ...')
print()

ecard = e.pick()
print(ecard)
print(); print()

print('attempting to pick from old deck again...')
print()

dcard = d.pick()
print(dcard)