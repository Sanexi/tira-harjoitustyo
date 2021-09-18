import unittest
from app import RPS, AI


class TestAI(unittest.TestCase):
    def setUp(self):
        self.ai = AI()
        self.game = RPS(self.ai)

    def test_constructor_creates_list(self):
        '''Test if AI-class creates a list'''

        self.assertEqual(self.ai.last_5_rounds, [])
    
    def test_ai_picks_correct_short(self):
        '''Test if AI picks scissors after player played rock the previous round, short game'''
        self.game.calculate(1)
        self.game.calculate(1)
        self.assertEqual(self.ai.pick(), 3)

    def test_ai_picks_correct_long(self):
        '''Test if AI picks scissors after player played rock the previous round, long game'''
        for i in range(100):
            self.game.calculate(3)
        self.assertEqual(self.ai.pick(), 2)


class TestRPS(unittest.TestCase):
    def setUp(self):
        self.ai = AI()
        self.game = RPS(self.ai)

    def test_correct_winner(self):
        '''Test if RPS picks right winner (0 = Tie)'''

        result = self.game.pick_winner(1, 1)
        self.assertEqual(result, 0)

    def test_correct_calculation(self):
        '''Test if RPS calculates the right winner.
        AI currently picks the one that would lose to players previous pick.
        Player should win.
        '''
        self.game.calculate(2)
        result = self.game.calculate(2)
        self.assertEqual(result, 2)
