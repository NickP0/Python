from poker.card import Card
from poker.deck import Deck
from poker.game import Game
from poker.hand import Hand
from poker.player import Player


deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)

hand1 = Hand()
hand2 = Hand()

player1 = Player(name = "Nick", hand = hand1)
player2 = Player(name = "Kim", hand = hand2)
players = [player1, player2]

game = Game(deck = deck, players = players)
game.play() 


for player in players:
    print(f"{player.name} receives a {player.hand}.")
    index, hand_name, hand_cards = player.best_hand()
    hand_cards_strings = [str(card) for card in hand_cards]
    hand_card_string = " and ".join(hand_cards_strings)
    print(f"{player.name} has a {hand_name} with a {hand_card_string}.")

winning_player = max(players)

print(f"The winner is {winning_player.name}.")
