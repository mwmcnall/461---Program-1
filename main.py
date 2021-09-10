from Hand import Hand
from Deck import Deck
from Simulator import Simulator


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Variables for main:
    cardNum = 13
    simNumber = 500
    playerResponse = "y"

    while (playerResponse.lower() == 'y'):
        # Create Classes to use
        hand = Hand()
        deck = Deck()

        # Deal 13 cards to Player
        for _ in range(cardNum):
            hand.AddCard(deck.DealCard())

        simulator = Simulator(deck.GetCurrentDeck())
        hand.PrintInfo()

        simulator.RunSimulation(simNumber, hand.points)

        playerResponse = input("Another hand[Y/N]?")

    print("--> Program exiting. <--")