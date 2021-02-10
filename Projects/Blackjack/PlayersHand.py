from cards import Cards

cards_pack = Cards()


class PlayersHand:
    sum_of_cards = 0

    def __init__(self, user="dealer") -> None:
        self.user = user

    def get_card(self):
        new_card = cards_pack.get_card()
        # ace can 11 or 1 it depends on users hand score
        if self.sum_of_cards <= 10 and new_card == 1:
            self.sum_of_cards += 11
        else:
            self.sum_of_cards += new_card
        print(f"{self.user}'s total value is: {self.sum_of_cards}\n")
