from random import randint
from os import system, name

class Cards():
    
    #DICTIONARY WITH CARDS:
    cards = {1 :"ace",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"jack",12:"queen",13:"king"}

    def print_your_card(self,value_of_card):
        print(f"Picked card is {self.cards[value_of_card]}")

    def get_card(self):
        value_of_card = randint(1,13)
        self.print_your_card(value_of_card)
        return value_of_card

class PlayersHand():
    sum_of_cards = 0

    def __init__(self,user="dealer") -> None:
        self.user = user

    def get_card(self):
        new_card = cards_pack.get_card()
        #ace can 11 or 1 it depends on users hand score
        if self.sum_of_cards <= 10 and new_card == 1:
            self.sum_of_cards += 11
        else:
            self.sum_of_cards += new_card
        print(f"{self.user}'s total value is: {self.sum_of_cards}\n")
        
def overleaped(total):
    return total > 21

def clear():
    # for windows 
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix') 
    else:
        _ = system('clear')

def user_input():
    choice = input("<Y> <N>:").upper()
    if choice == 'Y':
        return True
    else:
        return False

def get_money_input():
    global money
    betted_money = 0
    print(f"You have {money}$")
    while True:
        try:
            betted_money = int(input("Please enter money you want to bet: "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            if(money >= betted_money):
                break
            else:
                print("You don't have enough money to bet")
    return betted_money

def start_game(betted_money):
    global money
    overeached_cards_value = False
    player_hand = PlayersHand("Jakub")
    dealers_hand = PlayersHand()
    #While till users dont want to draw another card
    while True:
        #draw one card
        player_hand.get_card()
        #check if 21 is not overleaped
        if overleaped(player_hand.sum_of_cards):
            print("dealer win player overlaped")
            money -= betted_money
            return
        dealers_hand.get_card()
        if overleaped(dealers_hand.sum_of_cards):
            print("user win dealer overlaped")
            money += betted_money
            return
        print("Do you want to draw another card?",end="")
        if user_input() is False:
            break
        clear()

    #if dealer has less card value than user he can draw another cards till he wins or overreach
    while(dealers_hand.sum_of_cards < player_hand.sum_of_cards):
        dealers_hand.get_card()
        if overleaped(dealers_hand.sum_of_cards):
            print("Player's wins")
            money += betted_money
            return
        elif dealers_hand.sum_of_cards > player_hand.sum_of_cards:
            print("Dealers wins")
            money -= betted_money
        elif player_hand.sum_of_cards == dealers_hand.sum_of_cards:
            print("BUST!")

cards_pack = Cards()
money = 100
while(True): 
    print(f"You start with: {money}$.") 
    print("Do you want to play?", end= "")
    if user_input() == False:
        break
    betted_money = get_money_input()
    start_game(betted_money)
    if money <= 0:
        print("You are out of balance")
        break

print(f"You ended with: {money}$.!")
