import random

class Deck:
    deck = []

    def __init__(self) -> None:
        self.generateDeck()

    def generateDeck(self) -> None:
        self.deck = list(range(1, 14)) * 4

    def getDeck(self) -> list:
        random.shuffle(self.deck)

        return self.deck