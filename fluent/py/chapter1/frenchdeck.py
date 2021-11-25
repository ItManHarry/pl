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