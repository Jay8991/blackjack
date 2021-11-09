
class Player:
    def __init__(self):
        self.player_cards = []
        self.total = 0
    
    def get_total(self): 
        self.total = 0  
        for i in range(len(self.player_cards)):
            for key in self.player_cards[i]:
                self.total += key 
        return self.total 
    
    def show_cards(self):
        print(f"Player Cards: {self.player_cards}")
