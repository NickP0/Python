import unittest

from poker.card import Card
from poker.validators import FourOfAKindValidator

class FourOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        self.ace_of_clubs = Card(rank = "Ace", suit = "Clubs")
        self.ace_of_diamonds = Card(rank = "Ace", suit = "Diamonds")
        self.ace_of_hearts = Card(rank = "Ace", suit = "Hearts")
        self.ace_of_spades = Card(rank = "Ace", suit = "Spades")



        self.cards = [
            Card(rank = "2", suit = "Hearts"),
            Card(rank = "5", suit = "Clubs"),
            Card(rank = "7", suit = "Hearts"),
            self.ace_of_clubs,
            self.ace_of_diamonds,
            self.ace_of_hearts,
            self.ace_of_spades          
        ]


    def test_determines_four_cards_of_one_rank_are_present(self):
        validator = FourOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )
    
    def test_returns_four_cards_with_same_rank(self):
        validator = FourOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.ace_of_clubs,
                self.ace_of_diamonds,
                self.ace_of_hearts,
                self.ace_of_spades  
            ]
        )