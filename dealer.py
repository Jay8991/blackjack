import random

class Dealer:
    def __init__(self):
        self.random_num_list = []
        self.dealer_cards = []
        self.total = 0
        self.random_num = 0

    def deal_card(self,deck):
        self.random_num = random.choice(range(1,54))
        # while random number is inside the list that means it has been selected before 
        # therefore, we want to keep looping until new number pops up
        while self.random_num in self.random_num_list:
            self.random_num = random.choice(range(1,54))
        self.random_num_list.append(self.random_num)
        card = deck.cards[self.random_num].get_card()
        return card
    
    def get_total(self):
        self.total = 0   
        for i in range(len(self.dealer_cards)):
            for key in self.dealer_cards[i]:
                self.total += key 
        return self.total 
    
    def show_cards(self):
        print(f"Dealer Cards: {self.dealer_cards}")

