import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame:
    import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.game = CardGame()
        self.card1 = Card("Diamonds", 1)
        self.card2 = Card("Spades", 10)
        self.card3 = Card("Hearts", 5)
        self.card4 = Card("Clubs", 3)
        self.cards = [self.card1, self.card2, self.card3, self.card4]

    def test_check_for_ace_true(self):
        self.assertTrue(self.game.check_for_ace(self.card1))

    def test_check_for_ace_false(self):
        self.assertFalse(self.game.check_for_ace(self.card2))

    def test_highest_card(self):
        self.assertEqual(self.game.highest_card(self.card1, self.card2), self.card2)
  
    def test_cards_total(self):
        self.assertEqual(self.game.cards_total(self.cards), "You have a total of 19")
