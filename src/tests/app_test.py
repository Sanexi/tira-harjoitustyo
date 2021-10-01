import unittest
from app import Models, Ensembler, Memory, RPS


class TestModels(unittest.TestCase):
    def setUp(self):
        self.mem = Memory()
        self.models = Models(self.mem)
        self.ensembler = Ensembler(self.models)
        self.game = RPS(self.ensembler, self.mem)

    def test_model_output(self):
        '''Tests get_models output.'''
        self.game.calculate(1)
        self.game.calculate(1)
        output = self.models.get_models()
        self.assertEqual(output, (3, 2, 1, 3))


class TestEnsembler(unittest.TestCase):
    def setUp(self):
        self.mem = Memory()
        self.models = Models(self.mem)
        self.ensembler = Ensembler(self.models)
        self.game = RPS(self.ensembler, self.mem)

    def test_ai_wins_same_pick(self):
        '''If player only picks the same pick, the AI will defeat the player.'''
        self.game.calculate(1)
        self.game.calculate(1)
        self.game.calculate(1)
        self.game.calculate(1)
        self.game.calculate(1)
        self.game.calculate(1)
        self.assertEqual(self.ensembler.pick(), 2)

    def test_ai_wins_pattern_pick(self):
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
        self.assertEqual(self.ensembler.pick(), 2)

    def test_correct_score_addition(self):
        '''Tests that Ensembler adds scores correctly.'''
        self.game.calculate(1)
        self.game.calculate(2)
        self.game.calculate(3)
        self.game.calculate(1)
        self.game.calculate(2)
        score = self.ensembler.get_score()
        self.assertTrue(max(score) < 5)


class TestMemory(unittest.TestCase):
    def setUp(self):
        self.mem = Memory()

    def test_correct_list_addition_short(self):
        '''Tests that list adds correctly.'''
        self.mem.add_result(1, 1, 0)
        self.assertEqual(len(self.mem.prev_rounds), 1)

    def test_correct_list_addition_long(self):
        '''Tests that list doesn't exceed 5 values.'''
        self.mem.add_result(1, 1, 0)
        self.mem.add_result(1, 1, 0)
        self.mem.add_result(1, 1, 0)
        self.mem.add_result(1, 1, 0)
        self.mem.add_result(1, 1, 0)
        self.mem.add_result(1, 1, 0)
        self.mem.add_result(1, 1, 0)
        self.assertEqual(len(self.mem.prev_rounds), 5)

    def test_correct_return(self):
        '''Tests that get_result works correctly.'''
        self.mem.add_result(1, 1, 0)
        result = self.mem.get_result()
        self.assertEqual(result, [(1, 1, 0)])


class TestRPS(unittest.TestCase):
    def setUp(self):
        self.mem = Memory()
        self.models = Models(self.mem)
        self.ensembler = Ensembler(self.models)
        self.game = RPS(self.ensembler, self.mem)

    def test_correct_winner(self):
        '''Test if RPS picks right winner (0 = Tie)'''

        result = self.game.pick_winner(1, 1)
        self.assertEqual(result, 0)

    def test_correct_calculation(self):
        '''Test if RPS calculation returns correct values.'''
        self.game.calculate(2)
        result = self.game.calculate(2)[0]
        self.assertTrue(result in (0, 1, 2))
