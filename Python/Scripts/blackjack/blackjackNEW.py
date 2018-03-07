from tkinter import *
import random

# initialize global variables used in deck and card creation
SUITS = ['S', 'H', 'D', 'C']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}


class Card:
    def __init__(self, suit, rank, count):
        # check if specified suit and rank exists within the
        # global SUIT and RANK variables
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
            self.count = count
        else:
            self.suit = None
            self.rank = None
            self.count = None
            print("Invalid card: ", suit, rank, count)

    def get_card(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def get_image(self):
        return PhotoImage(file = "cards/" + self.count)

    def get_count(self):
        return self.count


class Hand:
    def __init__(self):
        self.cards = []

    def get_hand(self):
        result = ""
        card_count = 0
        for card in self.cards:
            card_count += 1
            result += card.get_card()
            if card_count != len(self.cards):
                result += ", "

        return result

    def add_card(self, card):
        self.cards.append(card)

    def get_cards(self):
        return self.cards

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

    def get_deck(self):
        deck_list = ""
        for card in self.cards:
            deck_list += " " + card.get_card()

        return deck_list


class Blackjack:

    def __init__(self):
        self.player_hand = 0
        self.dealer_hand = 0
        self.deck = 0
        self.player_score = 0
        self.dealer_score = 0

        self.player_card_hit_count = 1
        self.dealer_card_hit_count = 1

        self.window = Tk()
        self.window.title("Blackjack")

        self.frame = Frame(self.window)
        self.frame.pack()
        self.safe_to_clear = False

        bt_deal = Button(self.frame, width = 20, height = 10, text="Deal", command = self.deal)
        bt_hit = Button(self.frame, width = 20, height = 10, text="Hit", command = self.hit)
        bt_stand = Button(self.frame, width = 20, height = 10, text="Stand", command = self.stand)

        bt_deal.grid(row = 1, column = 1, pady = 10)
        bt_hit.grid(row = 1, column = 2, pady = 10)
        bt_stand.grid(row = 1, column = 3, pady = 10)

        self.frame2 = Frame(self.window)
        self.frame2.pack()

        self.player_image_list = []
        self.player_label_list = []

        self.frame3 = Frame(self.window)
        self.frame3.pack()

        self.dealer_image_list = []
        self.dealer_label_list = []

        #
        self.frame4 = Frame(self.window)
        self.frame4.pack()

        # game status GUI
        self.game_status = Label(self.frame4, text="")
        self.game_status.pack()

        # dealer score GUI
        self.dealer_status = Label(self.frame4, text="Press Deal to start!")
        self.dealer_status.pack()

        # player score GUI
        self.player_status = Label(self.frame4, text ="")
        self.player_status.pack()

        self.window.mainloop()

    def clear(self):

        self.game_status["text"] = ""
        self.dealer_status["text"] = "Press Deal to start!"
        self.player_status["text"] = ""
         
        self.player_image_list.clear()
        for i in range(0, len(self.player_hand.cards)):
            self.player_label_list[i].grid_forget()
            self.player_label_list[i].destroy()
        self.player_label_list.clear()

        self.dealer_image_list.clear()
        for i in range(0, len(self.dealer_hand.cards)):
            self.dealer_label_list[i].grid_forget()
            self.dealer_label_list[i].destroy()
        self.dealer_label_list.clear()

        self.player_card_hit_count = 1
        self.dealer_card_hit_count = 1

    def deal(self):
        if self.safe_to_clear:
            self.clear()

        self.deck = Deck()
        self.deck.shuffle()

        self.player_hand = Hand()
        self.dealer_hand = Hand()

        self.player_hand.add_card(self.deck.deal_card())
        self.player_hand.add_card(self.deck.deal_card())

        self.dealer_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())

        for i in range(len(self.player_hand.cards)):
            self.player_image_list.append(PhotoImage(file="cards/" +
                                                          str(self.player_hand.cards[i].get_count()) + ".gif"))

        for i in range(len(self.player_hand.cards)):
            self.player_label_list.append(Label(self.frame3, image = self.player_image_list[i]))
            self.player_label_list[i].pack(side = LEFT)

        for i in range(len(self.dealer_hand.cards)):
            self.dealer_image_list.append(PhotoImage(file="cards/" +
                                                          str(self.dealer_hand.cards[i].get_count()) + ".gif"))

        for i in range(len(self.dealer_hand.cards)):
            self.dealer_label_list.append(Label(self.frame2, image = self.dealer_image_list[i]))
            self.dealer_label_list[i].pack(side = LEFT)

        self.dealer_status["text"] = "Dealer total: " + str(self.dealer_hand.get_value())
        self.player_status["text"] = "Player total: " + str(self.player_hand.get_value())

        self.get_player_values()

        self.safe_to_clear = True

    def hit(self):

        if self.player_hand.get_value() <= 21:
            self.player_hand.add_card(self.deck.deal_card())

        self.player_card_hit_count += 1
        self.player_image_list.append(PhotoImage(file="cards/" + str(
            self.player_hand.cards[self.player_card_hit_count].get_count()) + ".gif"))
        self.player_label_list.append(Label(self.frame3, image = self.player_image_list[self.player_card_hit_count]))
        self.player_label_list[self.player_card_hit_count].pack(side= LEFT)

        self.player_status["text"] = "Player total: " + str(self.player_hand.get_value())

        self.get_player_values()

        if self.player_hand.get_value() > 21:
            print("\nBusted!")

            self.game_status["fg"] = "red"
            self.game_status["text"] = "Player busted, dealer wins!"

            self.dealer_score += 1
            self.show_scores()

    def show_scores(self):
        print("\nPlayer:", self.player_score, "\nDealer:", self.dealer_score)

    def get_player_values(self):
        print("\nPlayer:", self.player_hand.get_hand(), "total:", self.player_hand.get_value())
        print("Dealer:", self.dealer_hand.get_hand(), "total:", self.dealer_hand.get_value())

    def stand(self):
        while self.dealer_hand.get_value() < 17:
            self.dealer_hand.add_card(self.deck.deal_card())
            self.dealer_card_hit_count += 1

            print(self.dealer_card_hit_count)
            for i in range(len(self.dealer_hand.cards)):
                print(self.dealer_hand.cards[i], end=" ")
            print(self.dealer_hand.cards[self.dealer_card_hit_count].get_count())
            self.dealer_image_list.append(
                PhotoImage(file="cards/" + str(self.dealer_hand.cards[self.dealer_card_hit_count].get_count()) + ".gif"))

            self.dealer_label_list.append(Label(self.frame2, image=self.dealer_image_list[self.dealer_card_hit_count]))
            self.dealer_label_list[self.dealer_card_hit_count].pack(side=LEFT)


        self.dealer_status["text"] = "Dealer total: " + str(self.dealer_hand.get_value())

        self.get_player_values()

        if self.dealer_hand.get_value() > 21:
            print("\nDealer busted, Player wins!")

            self.game_status["fg"] = "green"
            self.game_status["text"] = "Dealer busted, Player wins!"

            self.player_score += 1
            self.show_scores()

        else:
            if self.dealer_hand.get_value() == self.player_hand.get_value():
                print("\nTie!")

                self.game_status["fg"] = "black"
                self.game_status["text"] = "Tie!"

                self.show_scores()
            elif self.dealer_hand.get_value() >= self.player_hand.get_value() or self.player_hand.get_value() > 21:
                print("\nDealer wins!")

                self.game_status["fg"] = "red"
                self.game_status["text"] = "Dealer wins!"

                self.dealer_score += 1
                self.show_scores()
            else:
                print("\nPlayer wins!")

                self.game_status["fg"] = "green"
                self.game_status["text"] = "Player wins!"

                self.player_score += 1
                self.show_scores()



Blackjack().deal()

