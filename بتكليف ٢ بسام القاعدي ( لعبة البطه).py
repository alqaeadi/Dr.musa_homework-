import random
# Card class representing a card with value and suit
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value} of {self.suit}"

    # Evaluate points based on the card's value
    def evaluate_points(self):
        return 10 if self.value in ["Jack", "Queen", "King"] else (11 if self.value == "Ace" else self.value)


#======================###############





# Deck class representing a deck of cards
class Deck:
    suits = ["Diamonds", "Spades", "Hearts", "Clubs"]
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

    def __init__(self):
        self.deck = [Card(value, suit) for suit in self.suits for value in self.values]
        random.shuffle(self.deck)

    # Draw a card from the deck
    def draw_card(self):
        return self.deck.pop()



#-------===================================


# Player class representing a player with a hand of cards
class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name

    # Draw a card from the deck and add to the player's hand
    def draw(self, deck):
        self.hand.append(deck.draw_card())

    # Display the player's hand
    def show_hand(self):
        for card in self.hand:
            print(card)

    # Calculate the total points of the player's hand
    def evaluate_hand_points(self):
        return sum(card.evaluate_points() for card in self.hand)


#<><><<><><>><><>><><><><><><><><><><><><><



# Game execution
deck = Deck()
player = Player("Bobby")

# Drawing three cards
for _ in range(3):
    player.draw(deck)

# Show the hand and total points
player.show_hand()
print("Total hand points::", player.evaluate_hand_points())
