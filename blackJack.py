import random

class Card:
    def __init__(self, num, suit):
        self.num = num
        self.suit = suit
        if num > 10:
            self.value = 10
        else:
            self.value = num
    
    def __str__(self):
        if self.num == 11:
            return f"jack of {self.suit}"
        if self.num == 12:
            return f"queen of {self.suit}"
        if self.num == 13:
            return f"king of {self.suit}"
        if self.num == 1:
            return f"ace of {self.suit}"
        
        return f"{self.num} of {self.suit}"

class Player:
    def __init__ (self):
        self.hand = []
    def show(self):
        if len(self.hand) > 0:
            for card in self.hand:
                print(card)
        else:
            print("no cards")
    def hand_value(self):
        low_value = 0
        high_value = 0
        for card in self.hand:
            if card.num == 1:
                high_value += 11
                low_value += 1
            else:
                high_value += card.value
                low_value += card.value
        return low_value, high_value
    def turn(self):
        values = self.hand_value()
        if values[0] > 21:
            return "bust"
        action = None
        while action != "hit" and action != "stand" and action != "quit":
            action = input ("hit, stand, quit? ")
            if action != "hit" and action != "stand" and action != "quit":
                print("invalid action, try again")
        return action
        
class Dealer:
    def __init__(self):
        self.hand = []
    def show(self):
        if len(self.hand) > 0:
            print(self.hand[0])
            for i in range(1, len(self.hand)):
                print("hidden")
        else:
            print("no cards")
    def hand_value(self):
        low_value = 0
        high_value = 0
        for card in self.hand:
            if card.num == 1:
                high_value += 11
                low_value += 1
            else:
                high_value += card.value
                low_value += card.value
        return low_value, high_value
    def turn(self):
        return "stand"
class Game:
    def __init__(self):
        self.deck = []
        for suit in ["spades", "hearts", "clubs", "diamonds"]:
            for num in range (1, 14):
                card = Card(num, suit)
                self.deck.append(card)
        random.shuffle(self.deck)
        self.discard = []
        self.dealer = Dealer()
        self.player = Player()
    def deal(self):
        #discarding the currents hands of the player and the dealer
        self.discard.extend(self.player.hand)
        self.discard.extend(self.dealer.hand)
        self.player.hand = []
        self.dealer.hand = []

        #check if the deck has enough cards
        if len(self.deck) < 4:
            random.shuffle(self.discard)
            self.deck.extend(self.discard)
            self.discard = []

        #draw 4 cards from deck
        card1 = self.deck.pop()
        card2 = self.deck.pop()
        card3 = self.deck.pop()
        card4 = self.deck.pop()
        #give the first two cards to the player

        self.player.hand.append(card1)
        self.player.hand.append(card2)
        self.dealer.hand.append(card3)
        self.dealer.hand.append(card4)
    def draw(self):
        if len(self.deck) < 1:
            random.shuffle(self.discard)
            self.deck.extend(self.discard)
            self.discard = []
        return self.deck.pop()
    def display_hands(self):
        print()
        print("your cards")
        self.player.show()
        print()
        print("dealer's cards")
        self.dealer.show()
        print()
    def play(self):
        while True:
            self.deal()
            self.display_hands()
            if len(self.player.hand) == 2 and self.player.hand_value()[1] == 21:
                print("Blackjack you Win!!")
                input ("press any key to continue")
                continue
            action = None
            while action != "stand" and action != "bust" and action != "quit":
                action = self.player.turn()
                if action == "hit":
                    card = self.draw()
                    self.player.hand.append(card)
                    self.display_hands()
                    if self.player.hand_value()[0] > 21:
                        action = "bust"

            if action == "quit":
                break
            if action == "bust":
                print("player busts")
                input("press enter to continue")
                continue
            #dealers turn
            action = None
            while action != "stand" and action != "bust":
                action = self.dealer.turn()
            player_values = self.player.hand_value()
            player_finalvalue = player_values[0]
            if player_values[1] <= 21:
                player_finalvalue = player_values[1]
            dealer_values = self.dealer.hand_value()
            dealer_finalvalue = dealer_values[0]
            if dealer_values[1] <= 21:
                dealer_finalvalue = dealer_values[1]
            
            #determine the results

            if player_finalvalue > dealer_finalvalue:
                print("You Win!")
            elif dealer_finalvalue > player_finalvalue:
                print("dealer wins!")
            else:
                print("Tie!!!!!!")
            input("Press enter to continue")


game = Game()
game.play()