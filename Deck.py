import random
from Hand import Hand

# To keep track of all possible cards in a deck and deal them randomly when needed
class Deck:

    # Class variable to reference
    fullDeck = [
        "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AC",
        "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AD",
        "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AH",
        "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", "AS",
    ]

    def __init__(self, suppliedDeck = None):
        if suppliedDeck is None:
            self.deck = self.fullDeck.copy()
        else:
            self.deck = suppliedDeck

    # Shuffles deck, removes item from deck and returns it
    def DealCard(self):
        random.shuffle(self.deck)
        return self.deck.pop()

    # Resets the current deck to be a full 52 card set
    def ResetDeck(self):
        self.deck = self.fullDeck

    def GetCurrentDeck(self):
        return self.deck
