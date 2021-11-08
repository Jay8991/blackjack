import dealer as d
import player as p
import cards as c
import random

def get_total(cards):
    total = 0
    for i in range(len(cards)):
        for key in cards[i]:
            total += key 
    return total 


def main():

    print("Welcome to Blackjack Game!!")

    player_cards = []
    dealer_cards = []

    done = False
    while not done: 
        # init player and dealer
        dealer = d.Dealer()
        player = p.Player()

        # get deck of cards
        deck = c.Deck()

        # dealer will pick random 2 cards for player and random 2 cards for himself
        player_card_1 = dealer.deal_card(deck)
        player_card_2 = dealer.deal_card(deck)

        # appending to player cards list
        player_cards.append(player_card_1)
        player_cards.append(player_card_2)

        dealer_card_1 = dealer.deal_card(deck)
        dealer_card_2 = dealer.deal_card(deck)

        # appending to dealer cards list
        dealer_cards.append(dealer_card_1)
        dealer_cards.append(dealer_card_2)

        # print both player card and only one dealer card 
        print(f"Player Cards: {player_cards}") 
        print(f"Dealer Card 1: {dealer_card_1}")  
   
        # first time around
        player_total = get_total(player_cards)
        print(f"Your total is: {player_total}")
        if player_total== 21:
            print("BLACKJACKKK! YOU WONNN!")
            continue
        elif player_total > 21:
            print("You Lost :(")
            break
        
        user_choice = False
        while not user_choice: 
            # ask player if want to hit or stay
            hit_or_stand = input("Do you want to hit or stand?(h/s) ").lower()
            if hit_or_stand == 'h':
                player_cards.append(dealer.deal_card(deck))
                print(f"Player Cards: {player_cards}")
                player_total = get_total(player_cards)
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

        if player_total > 21:
            print("You Lost :(")
            break


        # player decides to stand
        dealer_over_16 = False
        while not dealer_over_16:
            print(f"Dealer Cards: {dealer_cards}")
            dealer_total = get_total(dealer_cards)
            print(f"Dealer's total: {dealer_total}")
            if dealer_total < 16:
                print("Dealer getting another card because total is less than 16")
                dealer_cards.append(dealer.deal_card(deck))
            else:
                dealer_over_16 = True

        # compare dealer and player cards
        print(f"Dealer Total: {dealer_total}, Player Total: {player_total}")
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