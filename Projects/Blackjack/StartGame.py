from os import name, system
from PlayersHand import PlayersHand

betted_money = 0


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




class Game:

    def __init__(self,money):
        self.money = money

    @staticmethod
    def overleaped(total):
        return total > 21

    def start_game(self):
        global betted_money
        global money
        player_hand = PlayersHand("Jakub")
        dealers_hand = PlayersHand()
        # While till users dont want to draw another card
        while True:
            # draw one card
            player_hand.get_card()
            # check if 21 is not overreached
            if self.overleaped(player_hand.sum_of_cards):
                print("dealer win player overreached")
                self.money -= betted_money
                return
            dealers_hand.get_card()
            if self.overleaped(dealers_hand.sum_of_cards):
                print("user win dealer overreached")
                self.money += betted_money
                return
            print("Do you want to draw another card?", end="")
            if user_input() is False:
                break
            clear()

        # if dealer has less card value than user he can draw another cards till he wins or overreach
        while dealers_hand.sum_of_cards < player_hand.sum_of_cards:
            dealers_hand.get_card()
            if self.overleaped(dealers_hand.sum_of_cards):
                print("Player's wins")
                self.money += betted_money
                return
            elif dealers_hand.sum_of_cards > player_hand.sum_of_cards:
                print("Dealers wins")
                self.money -= betted_money
            elif player_hand.sum_of_cards == dealers_hand.sum_of_cards:
                print("BUST!")

    def get_money_input(self):
        global betted_money
        print(f"You have {self.money}$")
        while True:
            try:
                betted_money = int(input("Please enter money you want to bet: "))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            else:
                if self.money >= betted_money:
                    break
                else:
                    print("You don't have enough money to bet")
        return betted_money

    def new_game(self):
        global money, betted_money
        while True:
            print(f"You start with: {self.money}$.")
            print("Do you want to play?", end="")
            if not user_input():
                break
            betted_money = self.get_money_input()
            self.start_game()
            if self.money <= 0:
                print("You are out of balance")
                break
        print(f"You ended with: {self.money}$.!")

   