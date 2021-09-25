import random

class Models:
    '''Class that controls the AI and it's decisions'''

    def __init__(self, memory):
        self.memory = memory

    def model_0(self):
        '''Model 0: Chooses what would've lost to player's previous choice.'''
        last = self.memory.get_result()
        if len(last) == 0:
            self.m0_pick = random.randint(1, 3)
        else:
            self.m0_pick = last[-1][0]
            if self.m0_pick == 1:
                self.m0_pick += 2
            else:
                self.m0_pick -= 1
    
    def model_1(self):
        '''Model 1: Chooses what would've won player's previous choice.'''
        last = self.memory.get_result()
        self.m1_pick = last[-1][0]
        if self.m1_pick == 3:
            self.m1_pick = 1
        else:
            self.m1_pick += 1

    def model_2(self):
        '''Model 2: Chooses what would've tied with player's previous choice.'''
        last = self.memory.get_result()
        self.m2_pick = last[-1][0]

    #TODO: Vector model: player plays in certain pattern rock-scissors, scissors-paper, paper-rock, vector = +2
        #Least frequent model: beat players least frequent pick
        
    def get_models(self):
        '''Returns all modelpicks to the Ensembler'''
        last = self.memory.get_result()
        self.model_0()
        if len(last) == 0:
            return [self.m0_pick]
        self.model_1()
        self.model_2()
        return (self.m0_pick, self.m1_pick, self.m2_pick)
        

class Ensembler:
    '''Ensembler chooses the best model for all situations.'''
    def __init__(self, models):
        '''Ensembler constructor

        Args:
            models: class that holds different models for the Ensembler to decide which to use.'''

        self.models = models
        self.round = 0

        #Model scores:
        self.scores = [0, 0, 0]

    def pick(self):
        '''Decides which model the Ensembler should pick.
        First round plays random, otherwise checks the scores of different models.
        
        Returns:
            Ensembler's pick
        '''
        model_pick = self.models.get_models()
        if self.round == 0:
            pick = model_pick[0]
        else:
            model = self.scores.index(max(self.scores))
            pick = model_pick[model]
        self.round += 1
        return pick

    def add_score(self, player_pick):
        '''Keeps scoring for every model, ensembler uses the scores to play against the player.
        Gives score to all models depending on if they choose wrong or right.
        #TODO: Ensembler should only remember the last 5 rounds.
        
        Args:
            player_pick: What player picked this round. Compares this to models' picks.
        '''

        model_pick = self.models.get_models()
        if player_pick == 3:
            correct_pick = 1
        else:
            correct_pick = player_pick + 1
        for i in model_pick:
            if i == correct_pick:
                ind = model_pick.index(i)
                self.scores[ind] += 1
            if i != correct_pick and i != player_pick:
                ind = model_pick.index(i)
                self.scores[ind] -= 1



class Memory:
    '''Memory to remember earlier rounds.'''
    def __init__(self):
        self.last_5_rounds = []

    def add_result(self, player_pick, ai_pick, result):
        '''Adds a result to memory for later use and learning.
        Memory is kept only 5 rounds long, later rounds will be removed.
        Picks are stored as a number value:
            1 = Rock, 2 = Paper, 3 = Scissors
        Results are stored in numbers as well:
            0 = Tie, 1 = AI Wins, 2 = Player Wins
        '''

        if len(self.last_5_rounds) < 5:
            self.last_5_rounds.append((player_pick, ai_pick, result))
        else:
            self.last_5_rounds.pop(0)
            self.last_5_rounds.append((player_pick, ai_pick, result))
        

    def get_result(self):
        return self.last_5_rounds



class RPS:
    '''Creates the fountation for the game.'''
    def __init__(self, ensembler, memory):
        '''Rock-paper-scissors gameconstructor
        
        Args:
            ai: Ensembler that will use the right model to defeat the player.
            memory: class to store previous rounds.'''

        self.ai = ensembler
        self.memory = memory
        self.round = 0

    def calculate(self, player_pick):
        '''Asks the AI what it picks for this round using the method in AI-class.
        Combines it with the players pick to send it to pick_winner to get the result.
        add_score: Ensembler scores all models depending on the result.
        add_result: Adds outcome to Memory
        
        Args:
            player_pick: What the player has picked:
                1 = Rock, 2 = Paper, 3 = Scissors

        Returns:
            result: If AI or the player won or they tied:
                0 = Tie, 1 = AI Wins, 2 = Player Wins
        '''

        ai_pick = self.ai.pick()
        if self.round != 0:
            self.ai.add_score(player_pick)
        result = self.pick_winner(player_pick, ai_pick)
        self.memory.add_result(player_pick, ai_pick, result)

        self.round += 1
        return result, ai_pick


    def pick_winner(self, player_pick, ai_pick):
        '''Goes through every combination of picks and returns the result of the round.

        Args:
            ai_pick: What the AI has picked
            player_pick: What the player has picked
                1 = Rock, 2 = Paper, 3 = Scissors

        Returns:
            result: If AI or the player won or they tied:
                0 = Tie, 1 = AI Wins, 2 = Player Wins
        '''
        #Ties:
        if player_pick == ai_pick:
            return 0

        #AI wins:
        if player_pick == 1 and ai_pick == 2:
            return 1
        if player_pick == 2 and ai_pick == 3:
            return 1
        if player_pick == 3 and ai_pick == 1:
            return 1

        #AI wins:
        if player_pick == 1 and ai_pick == 3:
            return 2
        if player_pick == 2 and ai_pick == 1:
            return 2
        if player_pick == 3 and ai_pick == 2:
            return 2


'''
#Temporary system to run the game on the console:
mem = Memory()
ai = Models(mem)
ensembler = Ensembler(ai)
machine = RPS(ensembler, mem)
print("1 = Rock")
print("2 = Paper")
print("3 = Scissors")
print("0 = Exit")
player_wins = 0
ai_wins = 0
ties = 0

while True:
    player_pick = int(input(""))
    if player_pick == 0: break

    result = machine.calculate(player_pick)
    if result[0] == 0:
        print("It's a tie!")
        ties += 1
    if result[0] == 1:
        print("AI wins!")
        ai_wins += 1
    if result[0] == 2:
        print("You win!")
        player_wins += 1

    if result[1] == 1:
        print("AI's pick: Rock")
    if result[1] == 2:
        print("AI's pick: Paper")
    if result[1] == 3:
        print("AI's pick: Scissors")



    print(f"Total: W:{player_wins} T:{ties} L:{ai_wins}")
    print(ensembler.scores)
    print("")
'''

"""
for later use:

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Heipparallaa!"
"""
