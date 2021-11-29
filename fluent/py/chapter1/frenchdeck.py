import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JKQA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        print('Ranks : ', self.ranks)
        print('Suits : ', self.suits)
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
bear_card = Card('7', 'diamonds')
print(bear_card)
print('-' * 80)
deck = FrenchDeck()
print('Decks : ', len(deck))
for d in deck:
    print(d)
print('-' * 80)
print('First deck : ', deck[0])
print('Last deck : ', deck[-1])
print('Cards count is : ', len(deck))
from random import choice
print('Random card is : ', choice(deck))
print(deck[:3])
print(deck[12:13])
print(deck[12::13])
for d in reversed(deck):
    print('Deck is : ', d)
print(Card('Q', 'hearts') in deck)
print(Card('7', 'beasts') in deck)
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
for c in sorted(deck, key=spades_high):
    print('Card is : ', c)