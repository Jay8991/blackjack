import dealer as d
import player as p
import cards as c


def instructions():
    print("""Welcome to BlackJack Game.
You will be playing against the dealer and to 
win the game your cards total needs to be higher 
than the dealer.
    """)

def main():
    print("*" * 60)
    instructions()
    print("*" * 60)

    done = False
    while not done: 
        # init player and dealer
        dealer = d.Dealer()
        player = p.Player()

        # get deck of cards
        deck = c.Deck()

        # appending to player cards list
        player.player_cards.append(dealer.deal_card(deck))
        player.player_cards.append(dealer.deal_card(deck))

        dealer_card_1 = dealer.deal_card(deck)
        # appending to dealer cards list
        dealer.dealer_cards.append(dealer_card_1)
        dealer.dealer_cards.append(dealer.deal_card(deck))

        # print both player card and only one dealer card 
        print("*" * 40)
        player.show_cards()
        print(f"Dealer Card 1: {dealer_card_1}")  
        print("*" * 40)
   
        # first time around
        player_total = player.get_total()
        print(f"Your total is: {player_total}")
        print("*" * 40)
        if player_total == 21:
            print("BLACKJACKKK! YOU WONNN!")
        
        user_choice = False
        while not user_choice: 
            # ask player if want to hit or stay
            hit_or_stand = input("Do you want to hit or stand?(h/s) ").lower()
            if hit_or_stand == 'h':
                player.player_cards.append(dealer.deal_card(deck))
                player.show_cards()
                player_total = player.get_total()
                print(f"Your total is: {player_total}")
                if player_total > 21:
                    print("You Lost :(")
                    break
                elif player_total == 21:
                    print("You won!!")
                    break
                else:
                    continue
            elif hit_or_stand == 's':
                user_choice = True
            else:
                print("Invalid choice!!")


        # player decides to stand
        if((player_total < 21) ):
            while dealer.get_total() < 16:
                print("*" * 40)
                dealer.show_cards()
                dealer_total = dealer.get_total()
                print(f"Dealer Total: {dealer_total}")
                print("Dealer getting another card because total is less than 16")
                dealer.dealer_cards.append(dealer.deal_card(deck))
                print("*" * 40)
            
            if dealer.get_total() > 21:
                dealer.show_cards()
                print("Dealer went over 21!!")
                dealer_total = dealer.get_total()
                print(f"Dealer Total: {dealer_total}")
                print("Player Wins!!")
            else:
                # compare dealer and player cards
                print("*" * 40)
                print("These are the dealer's cards: ")
                dealer.show_cards()
                print("These are the player's cards: ")
                player.show_cards()
                print("*" * 40)
                dealer_total = dealer.get_total()
                print(f"Dealer Total: {dealer_total}, Player Total: {player_total}")
                print("*" * 40)
                if dealer_total > player_total:
                    print("Dealer Won!!!")
                elif player_total > dealer_total:
                    print("You Won!!")
                else:
                    print("It's a Draw")

        confirm = input("Do you want to continue?(y/n) ").lower()
        while True:
            if confirm == 'y':
                break
            elif confirm == 'n':
                done = True
                break
            else:
                print("Invalid!! Try Again")
    
    print("Thank you for playing!")

main()