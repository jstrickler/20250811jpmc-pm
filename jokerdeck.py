from abc import ABCMeta, abstractmethod
from card import Card
from carddeck import CardDeck

class GameEquipment(metaclass=ABCMeta):
    @abstractmethod
    def play(self):
        ...

class JokerDeck(GameEquipment, CardDeck):  # JokerDeck inherits from CardDeck
    def _make_deck(self):
        super()._make_deck()
        for joker_number in 1, 2:
            card = Card(f"JOKER-{joker_number}", "**JOKER**")
            self._cards.append(card)

    def play(self):
        print("playing...")
        
if __name__ == "__main__":
    j1 = JokerDeck()
    j1.shuffle()
    print(j1.cards)
    print(len(j1))
    j1.play()
    print(f"{JokerDeck.mro() = }")
    j1.doit()