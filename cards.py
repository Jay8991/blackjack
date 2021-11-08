
# suit for the cards
suits = ["spades", "diamond", "clover", "hearts"]

class Card:
    def __init__(self, face_value, suit):
        # card will be a dict with key being face_value and value being suit
        self.card = {face_value: suit}
        
    # get function so I can get the card  
    def get_card(self):
        return self.card

class Deck():
    def __init__(self):
        self.cards = {}
        self.card_number = 0
        for suit in suits:
            for value in range(1,14):
                self.card_number += 1
                self.cards[self.card_number] = Card(value, suit)

# {1: {1:"spades"}}