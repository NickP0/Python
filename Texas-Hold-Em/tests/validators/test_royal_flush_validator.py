import unittest

from poker.card import Card
from poker.validators import RoyalFlushValidator

class RoyalFlushValidatorTest(unittest.TestCase):
    def test_validates_cards_do_not_have_straight_flush_ending_in_ace(self):
        cards = [
            Card(rank = "9", suit = "Spades"),
            Card(rank = "10", suit = "Spades"), 
            Card(rank = "Jack", suit = "Spades"), 
            Card(rank = "Queen", suit = "Spades"), 
            Card(rank = "King", suit = "Spades"), 
            Card(rank = "Ace", suit = "Diamonds")
        ]

        validator = RoyalFlushValidator(cards = cards) 

        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_validates_cards_do_not_have_straight_flush_ending_in_ace(self):
        cards = [
            Card(rank = "2", suit = "Clubs"),
            Card(rank = "10", suit = "Spades"), 
            Card(rank = "Jack", suit = "Spades"), 
            Card(rank = "Queen", suit = "Spades"), 
            Card(rank = "King", suit = "Spades"), 
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "Ace", suit = "Diamonds")
        ]

        validator = RoyalFlushValidator(cards = cards) 

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_five_straight_cards_with_same_rank_ending_in_ace(self):
        ten = Card(rank = "10", suit = "Spades")
        jack = Card(rank = "Jack", suit = "Spades") 
        queen = Card(rank = "Queen", suit = "Spades") 
        king = Card(rank = "King", suit = "Spades") 
        ace = Card(rank = "Ace", suit = "Spades")

        cards = [
            Card(rank = "2", suit = "Clubs"),
            ten,
            jack,
            queen,
            king,
            ace,
            Card(rank = "Ace", suit = "Diamonds")
        ]

        validator = RoyalFlushValidator(cards = cards) 

        self.assertEqual(
            validator.valid_cards(),
            [
                ten,
                jack,
                queen,
                king,
                ace
            ]
        )