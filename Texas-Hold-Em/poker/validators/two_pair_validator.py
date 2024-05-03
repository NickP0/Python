from poker.validators import RankValidator

class TwoPairValidator(RankValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Two Pair"

    def is_valid(self):
        ranks_with_pairs = self._ranks_with_count(2) # { "5": 2, "Jack": 2 }
        return len(ranks_with_pairs) >= 2
    # if we have at least 2 key value pairs then we have a two pair

    def valid_cards(self):
        ranks_with_pairs = self._ranks_with_count(2) # { "5": 2, "Jack": 2 }
        cards = [card for card in self.cards if card.rank in ranks_with_pairs.keys()]
        return cards 

    # def _ranks_with_count(self, count):
    #     return {
    #         key: value 
    #         for key, value in self._card_rank_counts.items() 
    #         if value == count
    #     }
    
    # @property
    # def _card_rank_counts(self):
    #     card_rank_counts = {}
    #     for card in self.cards:
    #         card_rank_counts.setdefault(card.rank, 0)
    #         card_rank_counts[card.rank] += 1
    #     return card_rank_counts

