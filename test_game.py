import unittest
from Player import Player
from Game import Game
from unittest.mock import patch

class TestRockPaperScissors(unittest.TestCase):

    #tests that the code validates user inputs an integer
    @patch('builtins.input', side_effect=['1'])
    def test_input(self, mock_input):
        examplePlayer1 = Player("marie", 10)
        playerList = []
        game = Game(examplePlayer1, playerList)

        self.assertEqual(2, game.validate_input_int('2'))
        self.assertEqual(4, game.validate_input_int('4'))
        self.assertEqual(1,game.validate_input_int('y'))

    #test that the logic of the game works with the code
    def test_wining(self):
        examplePlayer1 = Player("marie", 10)
        playerList = []
        game = Game(examplePlayer1, playerList)
        self.assertEqual((True, 'Computer wins'), game.winning(2,3))
        self.assertEqual((True, 'Computer wins'), game.winning(3,1))
        self.assertEqual((True, 'Computer wins'), game.winning(1,2))
        # test that the player mins value gets updated with a win
        self.assertEqual((True, 'marie has won 11 games!'), game.winning(1,3))
        self.assertEqual((False, 'Tie, try again'), game.winning(1,1))
        self.assertEqual((False, 'Tie, try again'), game.winning(2,2))
        self.assertEqual((False, 'Tie, try again'), game.winning(3,3))

    #test user input function
    @patch('builtins.input', side_effect=['1'])
    def test_try_again(self, mock_input):
        examplePlayer1 = Player("marie", 10)
        playerList = []
        game = Game(examplePlayer1, playerList)

        self.assertEqual('1', game.tryAgain())
