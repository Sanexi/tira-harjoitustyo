from classes import Models, Ensembler, Memory, RPS


class Constructor:
    def __init__(self):
        self.mem = Memory()
        self.models = Models(self.mem)
        self.ensembler = Ensembler(self.models)
        self.game = RPS(self.ensembler, self.mem)
        self.score = [0, 0, 0]

    def play(self, input):
        '''Returns:
            result: result[0]: 0 = tie, 1 = ai win, 2 = player win
                    result[1]: 1 = ai picked rock, 2 = ai picked paper, 3 = ai picked scissors
        '''
        result = self.game.calculate(input)
        self.score[result[0]] += 1
        return result

    def get_ai_score(self):
        '''Returns:
            Scores of all models, index = model.'''
        return self.ensembler.get_score()

    def get_ai_modelpicks(self):
        '''Returns:
            What different models will pick for next round.'''
        return self.models.get_models()

    def get_score(self):
        return self.score
