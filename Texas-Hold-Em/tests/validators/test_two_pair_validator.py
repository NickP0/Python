import unittest

from poker.card import Card
from poker.validators import TwoPairValidator

class TwoPairValidatorTest(unittest.TestCase):
    def setUp(self):
        self.two_of_spades = Card(rank = "2", suit = "Spades")
        self.five_of_clubs = Card(rank = "5", suit = "Clubs")
        self.five_of_diamonds = Card(rank = "5", suit = "Diamonds")
        self.jack_of_hearts = Card(rank = "Jack", suit = "Hearts")
        self.jack_of_spades = Card(rank = "Jack", suit = "Spades")

        self.cards = [
            self.two_of_spades,
            self.five_of_clubs,
            self.five_of_diamonds,
            self.jack_of_hearts,
            self.jack_of_spades
        ]

    def tests_validates_cards_are_a_two_pair(self):
        validator = TwoPairValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )
    
    def test_returns_collection_of_cards_that_have_pairs(self):
        validator = TwoPairValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.five_of_clubs,
                self.five_of_diamonds,
                self.jack_of_hearts,
                self.jack_of_spades
            ]
        )