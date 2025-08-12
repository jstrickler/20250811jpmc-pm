import random
from card import Card

class CardDeck:
    SUITS = "Clubs Diamonds Hearts Spades".split()
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

    def __init__(self):
        self._make_deck()
    
    def _make_deck(self):
        self._cards = []  # private instance variable
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):  # public property
        return tuple(self._cards)

    def draw(self):
        return self._cards.pop()  # return next card

    def shuffle(self):
        random.shuffle(self._cards)

    def __len__(self):  # len(x)
        return len(self._cards)

    def __str__(self):
        return f"{self.__class__.__name__}:{len(self)}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}()"

    @classmethod
    def get_ranks(cls):
        return cls.RANKS
    
    @classmethod
    def get_suits(cls):
        return cls.SUITS

if __name__ == "__main__":
    d1 = CardDeck()
    print(d1)
    d1.shuffle()
    print(d1.cards)  # not d1.cards()
    for i in range(5):
        card = d1.draw()
        print(card)
    print(len(d1.cards))
    print(len(d1._cards))  # very naughty
    print(len(d1))
    print(d1)
    print(f"{d1 = }")
    print(d1.get_ranks())
    print(CardDeck.get_ranks())
