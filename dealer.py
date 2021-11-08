import random
import cards

class Dealer:
    def __init__(self):
        self.random_num_list = []

    def deal_card(self,deck):
        random_num = random.choice(range(1,54))

        # while random number is inside the list that means it has been selected before 
        # therefore, we want to keep looping until new number pops up
        while random_num in self.random_num_list:
            # print(self.random_num_list)
            random_num = random.choice(range(1,54))
        self.random_num_list.append(random_num)
        card = deck.cards[random_num].get_card()
        return card

