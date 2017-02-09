import unittest
from Player import Player
from Game import Game
from unittest.mock import patch

class TestRockPaperScissors(unittest.TestCase):

    # Enter y to play; enter 1 to throw rock; computer thows scissors
    @patch('Game.Game.compThrow', side_effect=[3])
    @patch('builtins.input', side_effect=['y', '1', 'n'])
    def test_game_win(self, mock_input, mock_comp_throw):
        examplePlayer1 = Player("marie", 10)
        playerList = []
        game = Game(examplePlayer1, playerList)
        game.go()
        self.assertCountEqual(game.playerList,  [ examplePlayer1])
        self.assertEqual(11, examplePlayer1.wins)
    @patch('Game.Game.compThrow', side_effect=[1])
    @patch('builtins.input', side_effect=['y', '3', 'n'])
    def test_game_lose(self, mock_input, mock_comp_throw):
        examplePlayer1 = Player("marie", 10)
        playerList = []
        game = Game(examplePlayer1, playerList)
        game.go()
        self.assertCountEqual(game.playerList,  [ examplePlayer1])
        self.assertEqual(10, examplePlayer1.wins)

    def test_game_tie_win(self):
        examplePlayer1 = Player("marie", 10)
        computerThrow = 1
        game = Game(examplePlayer1, [])
        self.assertFalse(game.winning(2 , 2))
        # player rock, computer scissors
        self.assertTrue(game.winning(1, 3))
        # test that player gets points
        self.assertEqual(11, examplePlayer1.wins)







if __name__ == '__main__':
    unittest.main()
