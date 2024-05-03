import unittest

from poker.card import Card
from poker.validators import PairValidator

class PairValidatorTest(unittest.TestCase):
    def test_validates_that_cards_are_a_pair(self):
        cards = [
            Card(rank = "Jack", suit = "Hearts"),
            Card(rank = "Jack", suit = "Diamonds")
        ]

        validator = PairValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )
    
    def test_returns_pair_from_card_collection(self):
        ten_of_spades = Card(rank = "10", suit = "Spades")
        ten_of_clubs = Card(rank = "10", suit = "Clubs") 

        cards = [
            Card(rank = "3", suit = "Hearts"),
            Card(rank = "5", suit = "Diamonds"),
            ten_of_clubs,
            ten_of_spades,
            Card(rank = "King", suit = "Clubs")
        ] 
        # need to sort cards that have the same rank -> sort by rank index and then sort alphabetically by suit

        validator = PairValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [ten_of_clubs, ten_of_spades]
        )

