from random import randint

class Cards():
    
    #DICTIONARY WITH CARDS:
    cards = {1 :"ace",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"jack",12:"queen",13:"king"}

    def print_your_card(self,value_of_card):
        print(f"Picked card is {self.cards[value_of_card]}")

    def get_card(self):
        value_of_card = randint(1,13)
        self.print_your_card(value_of_card)
        return value_of_card