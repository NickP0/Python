from poker.validators import ThreeOfKindValidator, PairValidator

class FullHouseValidator():
    def __init__(self, cards):
        self.cards = cards
        self.name = "Full House"
    

    def is_valid(self):
        return ThreeOfKindValidator(cards = self.cards).is_valid() and PairValidator(cards = self.cards).is_valid()
    
    def valid_cards(self):
        three_of_kind = ThreeOfKindValidator(cards = self.cards).valid_cards()

        pair = PairValidator(cards = self.cards).valid_cards()

        all_cards = three_of_kind + pair

        all_cards.sort()
        return all_cards
