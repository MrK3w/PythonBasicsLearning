from random import randint
from os import system, name

class Cards():
    
    #DICTIONARY WITH CARDS:
    cards = {1 :"ace",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"jack",12:"queen",13:"king"}

    def print_your_card(self,value_of_card):
        print(f"Pyicked card is {self.cards[value_of_card]}")

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
    choice = input("Do you want to draw another card? <Y> <N>: ").upper()
    if choice == 'Y':
        return True
    else:
        return False

cards_pack = Cards()
player_hand = PlayersHand("Jakub")
dealers_hand = PlayersHand()

while True:
    player_hand.get_card()
    if overleaped(player_hand.sum_of_cards):
        print("dealer win player overlaped 21")
        exit()
    dealers_hand.get_card()
    if overleaped(dealers_hand.sum_of_cards):
        print("user win dealer overlaped 21")
        exit()
    if user_input() is False:
        break
    clear()

print(f"{player_hand.user}'s total value is: {player_hand.sum_of_cards}")
print(f"{dealers_hand.user}'s total value is: {dealers_hand.sum_of_cards}\n")

if player_hand.sum_of_cards > dealers_hand.sum_of_cards:
    print("Player's wins")
else:
    print("Dealers wins")
