import unittest
from poker.card import Card


class CardTest(unittest.TestCase):
    def test_card_has_rank(self):
        card = Card(rank = "Queen", suit = "Hearts")
        self.assertEqual(card.rank, "Queen")
    
    def test_card_has_suit(self):
        card = Card(rank = "4", suit = "Spades")
        self.assertEqual(card.suit, "Spades")
    
    def test_knows_its_rank_index(self):
        card = Card(rank = "Jack", suit = "Hearts")
        self.assertEqual(card.rank_index, 9)
    
    def test_has_string_representation_with_rank_suit(self):
        card = Card("5", "Diamonds")
        self.assertEqual(str(card), "5 of Diamonds")
    
    def test_repr_string_representation_with_rank_suit(self):
        card = Card("5", "Diamonds")
        self.assertEqual(repr(card), 'Card("5", "Diamonds")')
    
    def test_card_has_four_possible_suits(self):
        self.assertEqual(
            Card.SUITS,
            ("Diamonds", "Spades", "Hearts", "Clubs")
        )
    
    def test_card_has_thirteen_possible_ranks(self):
        self.assertEqual(
            Card.RANKS,
            ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")
        )

    def test_card_only_allows_for_valid_rank(self):
        with self.assertRaises(ValueError):
            Card(rank = "Two", suit = "Hearts")
    
    def test_card_only_allows_for_valid_suit(self):
        with self.assertRaises(ValueError):
            Card(rank = "2", suit = "Not_a_suit")
    
    def test_can_create_standard_52_cards(self):
        cards = Card.create_standard_52_cards()
        self.assertEqual(len(cards), 52)

        self.assertEqual(
            cards[0],
            Card(rank = "2", suit = "Diamonds")
        )

        self.assertEqual(
            cards[-1],
            Card(rank = "Ace", suit = "Clubs")
        )
    
    def test_figures_out_if_two_cards_are_equal(self):
        self.assertEqual(
            Card(rank = "2", suit = "Diamonds"),
            Card(rank = "2", suit = "Diamonds")
        )
    
    
    def test_card_can_sort_itself_with_anohter(self):
        queen_of_spades = Card(rank = "Queen", suit = "Spades")
        king_of_spades = Card(rank = "King", suit = "Spades")

        evaluation = queen_of_spades < king_of_spades

        self.assertEqual(
            evaluation, True,
            "Sort algorithm isn't sorting the lower card first"
            )




    def test_sorts_cards(self):
        two_of_spades = Card(rank = "2", suit = "Spades")
        five_of_diamonds = Card(rank = "5", suit = "Diamonds")
        five_of_hearts = Card(rank = "5", suit = "Hearts")
        eight_of_hearts = Card(rank = "8", suit = "Hearts")
        ace_of_clubs = Card(rank = "Ace", suit = "Clubs")

        unsorted_cards = [
            five_of_hearts,
            five_of_diamonds,
            two_of_spades,
            ace_of_clubs,
            eight_of_hearts
        ]

        unsorted_cards.sort()

        self.assertEqual(
            unsorted_cards,
            [
                two_of_spades,
                five_of_diamonds,
                five_of_hearts,
                eight_of_hearts,
                ace_of_clubs
            ]
        )
        #already alphabetically sorted -> need to implement to __init__ on cards.py 