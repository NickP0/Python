from poker.validators import StraightFlushValidator

class RoyalFlushValidator():
    def __init__(self, cards):
        self.cards = cards
        self.name = "Royal Flush"

    def is_valid(self):
        straight_flush_validator = StraightFlushValidator(cards = self.cards)

        if straight_flush_validator.is_valid():
            straight_flush_cards = straight_flush_validator.valid_cards()
            is_royal = straight_flush_cards[-1].rank == "Ace"
            return is_royal
        
        return False
    
    def valid_cards(self):
        return StraightFlushValidator(cards = self.cards).valid_cards()

    
    # bug in Straight validator -> straight flush and royal flush is built upon -> always checking for straight by checking for batches of five cards in a row -> doesn't take into account for duplicate ranks