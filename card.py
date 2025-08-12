class Card:  # inherits from 'object'
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    # human-friendly
    def __str__(self):
        return f"Card:{self.rank}/{self.suit}"

    # code-friendly (how to reproduce the object)
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c1 = Card("8", "Diamonds")
    c2 = Card("A", "Hearts")
    print(c1)
    print(c2)
    print(c1.rank, c1.suit)
    # repr()
    cards = [c1, c2]
    print(cards)
    x = 5
    print(f"x is {x}")
    print(f"{x = }")
    print(f"{c1 = }")
    print(c1)
    print(c1.rank, c1.suit)
