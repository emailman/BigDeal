__author__ = 'emailman'


import random
import tkinter.messagebox


SUITS = "Spades Hearts Diamonds Clubs".split()
SUITS_SYMBOLS = "\u2660 \u2665 \u2666 \u2663".split()

RANKS = "Ace 2 3 4 5 6 7 8 9 10 Jack Queen King".split()

CARDS = 52
CARDS_PER_HAND = 13


def main():
    # Create a deck as a list of integers from 0 to 51
    deck = list(range(CARDS))

    # Shuffle the deck
    random.shuffle(deck)

    # Show the deck
    # print(deck)

    # Pop a card from the end of the deck
    card = deck.pop()
    # print(deck)

    # What card is it?
    # print(card)
    print("You got the", RANKS[card % CARDS_PER_HAND], "of",
          SUITS[card // CARDS_PER_HAND])

    # Show the card in a dialog box
    tkinter.messagebox.showinfo("Card Picked",
                                SUITS_SYMBOLS[card // CARDS_PER_HAND] + " " + RANKS[card % CARDS_PER_HAND])


main()
