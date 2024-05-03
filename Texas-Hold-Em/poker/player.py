class Player():
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    
    def __gt__(self, other):
        current_player_best_validator_index = self.best_hand()[0]
        other_player_best_validator_index = other.best_hand()[0]
        return current_player_best_validator_index < other_player_best_validator_index


    def best_hand(self):
        return self.hand.best_rank()
        
    def add_cards(self, cards):
        self.hand.add_cards(cards)
    
    def wants_to_fold(self):
        return False
    # input("") -> Continue or Fold?
    # Continue -> check how much to bet?
    # if self.wager < self.amount return true else: false

    # Attribute = how much money player has
    # Input -> how much does player want to bet?
    # Logic to figure out if wager is valid (see line 16)
    # Wager and wager being matched by second player
    # raise wager?
    
