from poker.validators import RankValidator

class ThreeOfKindValidator(RankValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Three of a Kind"
    
    def is_valid(self):
        ranks_with_three_of_kind = self._ranks_with_count(3) #{ "Queen": 3 }
        return len(ranks_with_three_of_kind) == 1

    def valid_cards(self):
        ranks_with_pairs = self._ranks_with_count(3) #{ "Queen": 3 }
        cards = [card for card in self.cards if card.rank in ranks_with_pairs.keys()]
        return cards