import unittest
from app import Models, Ensembler, Memory, RPS


class TestModels(unittest.TestCase):
    def setUp(self):
        self.mem = Memory()
        self.models = Models(self.mem)
        self.ai = Ensembler(self.models)
        self.game = RPS(self.ai, self.mem)

    def test_model_0(self):
        '''Tests that model 0 picks correct.'''
        self.game.calculate(1)
        self.models.model_0()
        pick = self.models.m0_pick
        self.assertEqual(pick, 3)

    def test_model_1(self):
        '''Tests that model 1 picks correct.'''
        self.game.calculate(1)
        self.models.model_1()
        pick = self.models.m1_pick
        self.assertEqual(pick, 2)

    def test_model_2(self):
        '''Tests that model 2 picks correct.'''
        self.game.calculate(1)
        self.models.model_2()
        pick = self.models.m2_pick
        self.assertEqual(pick, 1)

    def test_model_output(self):
        '''Tests get_models output.'''
        self.game.calculate(1)
        self.game.calculate(1)
        output = self.models.get_models()
        self.assertEqual(output, (3, 2, 1))


class TestEnsembler(unittest.TestCase):
    def setUp(self):
        self.mem = Memory()
        self.models = Models(self.mem)
        self.ai = Ensembler(self.models)
        self.game = RPS(self.ai, self.mem)
    
    def test_ai_wins_same_pick(self):
        '''If player only picks the same pick, the AI will defeat the player.'''
        self.game.calculate(1)
        self.game.calculate(1)
        self.game.calculate(1)
        self.game.calculate(1)
        self.game.calculate(1)
        self.game.calculate(1)
        self.assertEqual(self.ai.pick(), 2)

    def test_ai_wins_repeated_pick(self):
        '''If player repeats the same picks, the AI will defeat the player.'''
        self.game.calculate(1)
        self.game.calculate(2)
        self.game.calculate(3)
        self.game.calculate(1)
        self.game.calculate(2)
        self.game.calculate(3)
        self.game.calculate(1)
        self.game.calculate(2)
        self.game.calculate(3)
        self.game.calculate(1)
        self.game.calculate(2)
        self.game.calculate(3)
        self.assertEqual(self.ai.pick(), 2)

    def test_correct_score_addition(self):
        '''Tests that Ensembler adds scores correctly.'''
        self.game.calculate(1)
        self.game.calculate(2)
        self.game.calculate(3)
        self.game.calculate(1)
        self.game.calculate(2)
        m0_score = self.ai.scores[0]
        m1_score = self.ai.scores[1]
        m2_score = self.ai.scores[2]
        self.assertTrue(m0_score < 5 and m1_score < 5 and m2_score < 5)


class TestMemory(unittest.TestCase):
    def setUp(self):
        self.mem = Memory()
    
    def test_correct_list_addition_short(self):
        '''Tests that list adds correctly.'''
        self.mem.add_result(1, 1, 0)
        self.assertEqual(len(self.mem.last_5_rounds), 1)
    
    def test_correct_list_addition_long(self):
        '''Tests that list doesn't exceed 5 values.'''
        self.mem.add_result(1, 1, 0)
        self.mem.add_result(1, 1, 0)
        self.mem.add_result(1, 1, 0)
        self.mem.add_result(1, 1, 0)
        self.mem.add_result(1, 1, 0)
        self.mem.add_result(1, 1, 0)
        self.mem.add_result(1, 1, 0)
        self.assertEqual(len(self.mem.last_5_rounds), 5)

    def test_correct_return(self):
        '''Tests that get_result works correctly.'''
        self.mem.add_result(1, 1, 0)
        result = self.mem.get_result()
        self.assertEqual(result, [(1, 1, 0)])


class TestRPS(unittest.TestCase):
    def setUp(self):
        self.mem = Memory()
        self.models = Models(self.mem)
        self.ai = Ensembler(self.models)
        self.game = RPS(self.ai, self.mem)

    def test_correct_winner(self):
        '''Test if RPS picks right winner (0 = Tie)'''

        result = self.game.pick_winner(1, 1)
        self.assertEqual(result, 0)

    def test_correct_calculation(self):
        '''Test if RPS calculation returns correct values.'''
        self.game.calculate(2)
        result = self.game.calculate(2)[0]
        self.assertTrue(result == 0 or result == 1 or result == 2)
