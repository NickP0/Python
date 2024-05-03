from poker.validators import (
    RoyalFlushValidator,
    StraightFlushValidator,
    FourOfAKindValidator,
    FullHouseValidator,
    FlushValidator,
    StraightValidator,
    ThreeOfKindValidator,
    TwoPairValidator,
    PairValidator, 
    HighCardValidator, 
    NoCardsValidator
)

class Hand():
    VALIDATORS = (
        RoyalFlushValidator,
        StraightFlushValidator,
        FourOfAKindValidator,
        FullHouseValidator,
        FlushValidator,
        StraightValidator,
        ThreeOfKindValidator,
        TwoPairValidator,
        PairValidator, 
        HighCardValidator, 
        NoCardsValidator 
        )   
     
    def __init__(self):
        self.cards = []
    
    def __repr__(self):
        cards_as_strings = [str(card) for card in self.cards]
        return ", ".join(cards_as_strings)

    def add_cards(self, cards):
        copy_cards = self.cards[:]
        copy_cards.extend(cards)
        copy_cards.sort()
        self.cards = copy_cards

    def best_rank(self):
        for index, validator_cls in enumerate(self.VALIDATORS):
            validator = validator_cls(cards = self.cards)
            if validator.is_valid():
                return (index, validator.name, validator.valid_cards())

  


