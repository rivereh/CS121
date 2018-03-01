from tkinter import *
import random


player_score = 0
dealer_score = 0
player_hand = 0
dealer_hand = 0
window = 0
frame = 0
player_label = ""

SUITS = ['S', 'H', 'D', 'C']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}


class Card:
    def __init__(self, suit, rank, count):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
            self.count = count
        else:
            self.suit = None
            self.rank = None
            print("Invalid card: ", suit, rank, count)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def get_image(self):
        return PhotoImage(file = "card/" + self.count)


class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        result = ""
        card_count = 0
        for card in self.cards:
            card_count += 1
            result += card.__str__()
            if card_count != len(self.cards):
                result += ", "

        return result

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        contains_ace = False

        for card in self.cards:
            rank = card.get_rank()
            value += VALUES[rank]

            if rank == 'A':
                contains_ace = True

        if value < 11 and contains_ace:
            value += 10

        return value


class Deck:
    def __init__(self):
        self.cards = []

        card_count = 1
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank, card_count))
                card_count += 1

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop(0)

    def __str__(self):
        result = ""
        for card in self.cards:
            result += " " + card.__str__()

        return "Deck contains" + result


def deal():
    global player_hand, dealer_hand, deck, window, frame, player_label

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())

    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())

    player_label["text"] = player_hand


    print("\nPlayer:", player_hand, "total:", player_hand.get_value())
    print("Dealer:", dealer_hand, "total:", dealer_hand.get_value())

    '''choice = input("\nHit or stand? (h / s): ")
    if choice == 'h':
        hit()
    elif choice == 's':
        stand()'''


def hit():
    global player_score, dealer_score, player_hand, dealer_hand

    if player_hand.get_value() <= 21:
        player_hand.add_card(deck.deal_card())

    print("\nPlayer:", player_hand, "total:", player_hand.get_value())
    print("Dealer:", dealer_hand, "total:", dealer_hand.get_value())

    if player_hand.get_value() > 21:
        print("\nBusted!")
        dealer_score += 1
        show_scores()
        '''play_again = input("\nPlay again? (y / n): ")
        if play_again == 'y':
            deal()
        else:
            sys.exit()

    choice = input("\nHit or stand? (h / s): ")
    if choice == 'h':
        hit()
    elif choice == 's':
        stand()'''


def show_scores():
    global player_score, dealer_score
    print("\nPlayer:", player_score, "\nDealer:", dealer_score)


def stand():
    global player_score, dealer_score

    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(deck.deal_card())

    print("\nPlayer:", player_hand, "total:", player_hand.get_value())
    print("Dealer:", dealer_hand, "total:", dealer_hand.get_value())

    if dealer_hand.get_value() > 21:
        print("\nDealer busted, Player wins!")

        player_score += 1
        show_scores()
        '''play_again = input("\nPlay again? (y / n): ")
        if play_again == 'y':
            deal()
        else:
            sys.exit()'''
    else:
        if dealer_hand.get_value() >= player_hand.get_value() or player_hand.get_value() > 21:
            print("\nDealer wins!")
            dealer_score += 1
            show_scores()
            '''play_again = input("\nPlay again? (y / n): ")
            if play_again == 'y':
                deal()
            else:
                sys.exit()'''
        else:
            print("\nPlayer wins!")
            player_score += 1
            show_scores()
            '''play_again = input("\nPlay again? (y / n): ")
            if play_again == 'y':
                deal()
            else:
                sys.exit()'''


def main():

    global player_hand, dealer_hand, window, frame, player_label

    window = Tk()
    window.title("Blackjack")

    frame = Frame(window)
    frame.pack()

    player_label = Label(frame, text="")

    btDeal = Button(frame, width = 20, height = 10, text="Deal", command=deal)
    btHit = Button(frame, width = 20, height = 10, text="Hit", command=hit)
    btStand = Button(frame, width = 20, height = 10, text="Stand", command=stand)

    btDeal.grid(row=1, column=1)
    btHit.grid(row=1, column=2)
    btStand.grid(row=1, column=3)

    window.mainloop()

main()

