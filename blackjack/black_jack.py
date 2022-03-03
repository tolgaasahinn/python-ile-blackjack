import random
import time
from art import logo
import os

card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def game():
    clear()
    starts = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    while starts == "y":
        print(logo)
        print("Cards are giving...")
        time.sleep(1)
        user_cards = []
        dealer_cards = []
        for i in range(2):
            user_cards.append(random.choice(card))
            dealer_cards.append(random.choice(card))
        total_point_user = sum(user_cards)
        total_point_dealer = sum(dealer_cards)
        print(f"Your cards: {user_cards}, current score: {total_point_user}")
        print(f"Computer's first card: {dealer_cards[0]}")
        if total_point_dealer == 21:
            print(f"Computer's first card: {dealer_cards}")
            print("Computer has Blackjack computer win ...")
            game()
        elif total_point_user == 21 and total_point_dealer != 21:
            print("Congratulations. You got black jack you win the game.")
            game()
        add_card = input("Type 'y' to get another card, type 'n' to pass:")
        while add_card == "y":
            user_cards.append(random.choice(card))
            total_point_user = sum(user_cards)
            for i in user_cards:
                if i == 11 and total_point_user > 21:
                    i = 1
            total_point_user = sum(user_cards)
            print(f"Your cards: {user_cards}, current score: {total_point_user}")
            if total_point_user > 21:
                print(f"Computer's final hand: {dealer_cards}, final score: {total_point_dealer}")
                print("you lost dealer won")
                clear()
                game()
            add_card = input("Type 'y' to get another card, type 'n' to pass:")
        while total_point_dealer < 16:
            dealer_cards.append(random.choice(card))
            for i in dealer_cards:
                if i == 11 and total_point_dealer > 21:
                    i = 1
            total_point_dealer = sum(dealer_cards)
        if total_point_dealer > 21:
            print(f"Your cards: {user_cards}, current score: {total_point_user}")
            print(f"Computer's final hand: {dealer_cards}, final score: {total_point_dealer}")
            print("Opponent went over. You win")
        if total_point_dealer > total_point_user:
            print(f"Your cards: {user_cards}, current score: {total_point_user}")
            print(f"Computer's final hand: {dealer_cards}, final score: {total_point_dealer}")
            print("you lost dealer won")
        elif total_point_dealer < total_point_user:
            print(f"Your cards: {user_cards}, current score: {total_point_user}")
            print(f"Computer's final hand: {dealer_cards}, final score: {total_point_dealer}")
            print("you won the game")
        elif total_point_dealer == total_point_user:
            print("its draw")
        starts = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
        clear()

if __name__ == "__main__":
    game()
