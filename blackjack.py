import random


def deal_card():
    """This is to generate random card for the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#here we made 2 empty list as deck
dealer_deck=[]
player_deck=[]
is_game_over= False

def calculate_score(cards):
    """calculating score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(dealer_score,player_score):
    if player_score > 21 and dealer_score > 21:
        return "You went over. You lose 😤"

    if player_score == dealer_score:
        return "Draw 🙃"
    elif dealer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif player_score == 0:
        return "Win with a Blackjack 😎"
    elif player_score > 21:
        return "You went over. You lose 😭"
    elif dealer_score > 21:
        return "Opponent went over. You win 😁"
    elif player_score > dealer_score:
        return "You win 😃"
    else:
        return "You lose 😤"
    if player_score > 21 and dealer_score > 21:
        return "You went over. You lose 😤"


    if player_score == dealer_score:
        return "Draw 🙃"
    elif dealer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif player_score == 0:
        return "Win with a Blackjack 😎"
    elif player_score > 21:
        return "You went over. You lose 😭"
    elif dealer_score > 21:
        return "Opponent went over. You win 😁"
    elif player_score > dealer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

    
for __ in range(2):
    #giving players their deck
    dealer_deck.append(deal_card())
    player_deck.append(deal_card())

while not is_game_over:
    dealer_score = calculate_score(dealer_deck) #calculating score of dealer
    player_score = calculate_score(player_deck) #calculating score of player

    print(f"Your Deck {player_deck}")
    print(f"Dealer First Card {dealer_deck[0]}")

    if player_score==0 or dealer_score==0 or player_score>21:
        is_game_over= True
    else:
        user_should_deal = input("Do you want to hit(y)")
        if user_should_deal == "y":
            player_deck.append(deal_card())
            player_score = calculate_score(player_deck)
        else:
            is_game_over= True

while dealer_score != 0 and dealer_score<17:
    dealer_deck.append(deal_card())
    dealer_score = calculate_score(dealer_deck)
print(compare(dealer_score, player_score))