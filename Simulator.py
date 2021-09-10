from Deck import Deck
from Hand import Hand
from enum import Enum


class Counts(Enum):
    PASS = 0
    PART_SCORE = 1
    GAME = 2
    SMALL_SLAM = 3
    GRAND_SLAM = 4


class Simulator:

    def __init__(self, deckInfo):
        self.deck = Deck(deckInfo)
        # Save deck information for later
        self.originalDeck = deckInfo
        self.hand = Hand()
        self.counts = [0, 0, 0, 0, 0]
        self.simNumber = 0
        self.probabilities = [0, 0, 0, 0, 0]
        self.probNames = ["Pass"
            , "Part score"
            , "Game"
            , "Small Slam"
            , "Grand Slam"
                          ]

    # Deals self 13 cards
    def DealSelf(self):
        for _ in range(13):
            self.hand.AddCard(self.deck.DealCard())
        self.ResetDeck()

    def ResetDeck(self):
        self.deck.deck = self.originalDeck.copy()

    def ResetHand(self):
        self.hand = Hand()

    def RunSimulation(self, x_times, otherPoints):
        print("Running simulation.....\n")
        self.simNumber = x_times
        for _ in range(x_times):
            self.DealSelf()
            self.hand.CalculatePoints(otherPoints)
            if self.hand.points < 20:
                self.counts[Counts.PASS.value] += 1
            elif self.hand.points <= 25:
                self.counts[Counts.PART_SCORE.value] += 1
            elif self.hand.points <= 31:
                self.counts[Counts.GAME.value] += 1
            elif self.hand.points <= 35:
                self.counts[Counts.SMALL_SLAM.value] += 1
            elif self.hand.points >= 35:
                self.counts[Counts.GRAND_SLAM.value] += 1
            self.ResetHand()
        self.ConvertProbabilities()
        self.PrintProbabilities(x_times)

    def ConvertProbabilities(self):
        for index, count in enumerate(self.counts):
            self.probabilities[index] = (count / self.simNumber) * 100

    def PrintProbabilities(self, x_times):
        print("The estimated probability based on", x_times,"simulated hands:")
        for index, prob in enumerate(self.probabilities):
            print(self.probNames[index], ": ", end='')
            print('{0:.2f}%'.format(self.probabilities[index]))
        print()


    # Take an old deck of 39 cards
    # Run x number of simulations on that
    # Keeps track of counts for each point estimation
    # Converts those points into percentages to be readable
    # Prints that info
