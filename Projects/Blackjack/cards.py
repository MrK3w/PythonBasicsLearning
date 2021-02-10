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


def start_game():
    global players_win
    global dealers_win
    over = False
    player_hand = PlayersHand("Jakub")
    dealers_hand = PlayersHand()
    while True:
        player_hand.get_card()
        if overleaped(player_hand.sum_of_cards):
            over = True
            print("dealer win player overlaped")
            dealers_win +=1
            break
        dealers_hand.get_card()
        if overleaped(dealers_hand.sum_of_cards):
            over = True
            print("user win dealer overlaped")
            players_win += 1
            break
        print("Do you want to draw another card?",end="")
        if user_input() is False:
            break
        clear()
    print(f"{player_hand.user}'s total value is: {player_hand.sum_of_cards}")
    print(f"{dealers_hand.user}'s total value is: {dealers_hand.sum_of_cards}\n")
    if over == False:
        while(dealers_hand.sum_of_cards < player_hand.sum_of_cards):
            dealers_hand.get_card()
            print(f"{player_hand.user}'s total value is: {player_hand.sum_of_cards}")
            print(f"{dealers_hand.user}'s total value is: {dealers_hand.sum_of_cards}\n")
            if overleaped(dealers_hand.sum_of_cards):
                print("Player's wins")
                players_win += 1
    if player_hand.sum_of_cards > dealers_hand.sum_of_cards and over == False:
        print("Player's wins")
        players_win += 1
    elif dealers_hand.sum_of_cards > player_hand.sum_of_cards and over == False:
        print("Dealers wins")
        dealers_win +=1

cards_pack = Cards()
players_win = 0
dealers_win = 0
while(True): 
    print(f"Players wins: {players_win} Dealers wins: {dealers_win} ")   
    print("Do you want to play?", end= "")
    if user_input() == False:
        break
    start_game()

