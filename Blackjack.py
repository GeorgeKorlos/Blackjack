from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    choice = random.choice(cards)
    return choice

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0 # 0 means blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user, computer):
    if user == computer:
       return "Draw."
    elif computer == 21:
        return "Loss, dealer has Blackjack."
    elif user == 21:
        return "You win with a Blackjack!"
    elif user > 21:
        return "You went over. You lose."
    elif computer > 21:
        return "Dealer went over. You win"
    elif user > computer:
        return "You win!"
    else:
        return "You lose."
def play():

    print(logo)

    user_cards = []
    computer_cards = []

    game_over = False

    for card in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_outcome = calculate_score(user_cards)
        comp_outcome = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, score: {user_outcome}.")
        print(f"Dealer's card: {computer_cards[0]}.")

        if user_outcome == 0 or comp_outcome == 0 or user_outcome > 21:
            game_over = True
        else:
            more = input("Would you like to draw another card? If so type 'yes', if not type 'no': ")
            if more == 'yes':
                user_cards.append(deal_card())
            else:
                game_over = True
        
    while comp_outcome != 0 and comp_outcome < 17:
        computer_cards.append(deal_card())
        comp_outcome = calculate_score(computer_cards)


    print(f"Your hand {user_cards}, your final score: {user_outcome}")
    print(f"Dealer's hand {computer_cards}, dealer's final score: {comp_outcome}")
    print(compare(user=user_outcome,computer=comp_outcome))

while input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ") == 'yes':
    play()