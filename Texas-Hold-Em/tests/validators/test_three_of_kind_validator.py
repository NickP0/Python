import unittest

from poker.card import Card
from poker.validators import ThreeOfKindValidator 

class ThreeOfKindValidatorTest(unittest.TestCase):
    def setUp(self):
        three = Card(rank = "3", suit = "Clubs")
        eight = Card(rank = "8", suit = "Clubs")
        self.queen_of_diamonds = Card(rank = "Queen", suit = "Diamonds")
        self.queen_of_hearts = Card(rank = "Queen", suit = "Hearts")
        self.queen_of_spades = Card(rank = "Queen", suit = "Spades")

        self.cards = [
            three,
            eight,
            self.queen_of_diamonds,
            self.queen_of_hearts,
            self.queen_of_spades
        ]

    def test_validates_that_cards_have_exactly_three_of_same_rank(self):
        validator = ThreeOfKindValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
         )
    
    def test_returns_three_of_a_kind_from_card_collection(self):
        validator = ThreeOfKindValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.queen_of_diamonds,
                self.queen_of_hearts,
                self.queen_of_spades
            ]
        )