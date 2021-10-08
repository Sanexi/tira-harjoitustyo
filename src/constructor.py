from classes import Models, Ensembler, Memory, RPS

class Constructor:
    def __init__(self):
        self.mem = Memory()
        self.models = Models(self.mem)
        self.ensembler = Ensembler(self.models)
        self.game = RPS(self.ensembler, self.mem)

    def play(self, input):
        '''Returns:
            result: result[0]: 0 = tie, 1 = ai win, 2 = player win
                    result[1]: 1 = ai picked rock, 2 = ai picked paper, 3 = ai picked scissors
        '''
        result = self.game.calculate(input)
        return result

    def get_ai_score():
        '''Returns:
            Scores of all models, index = model.'''
        return self.ensembler.get_score()

    def get_ai_modelpicks():
        '''Returns:
            What different models will pick for next round.'''
        return self.models.get_models()
