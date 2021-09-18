import random

class AI:
    '''Class that controls the AI and it's decisions'''

    def __init__(self):
        self.last_5_rounds = []

    def pick(self):
        '''Decides what the AI should do.

        Currently on round 1: pick random,
        other rounds: pick what would lose to player's last pick
        
        Returns:
            AI's pick
        '''
        if len(self.last_5_rounds) == 0:
            return random.randint(1, 3)
        else:
            ai_pick = self.last_5_rounds[-1][0]
            if ai_pick == 1:
                ai_pick += 2
            else: ai_pick -= 1
            return ai_pick

    def add_result(self, player_pick, ai_pick, result):
        '''Adds a result to AI's memory for later use and learning.
        Memory is kept only 5 rounds long, later rounds will be removed.
        '''

        if len(self.last_5_rounds) <= 5:
            self.last_5_rounds.append((player_pick, ai_pick, result))
        else:
            self.last_5_rounds.pop(0)
            self.last_5_rounds.append((player_pick, ai_pick, result))


class RPS:
    '''Creates the fountation for the game'''
    def __init__(self, ai):
        '''Rock-paper-scissors game's constructor
        
        Args:
            ai: AI-class to be used in the game'''

        self.ai = ai
        self.round = 1

    def calculate(self, player_pick):
        '''Asks the AI what it picks for this round using the method in AI-class.
        Combines it with the players pick to send it to pick_winner to get the result.
        
        Args:
            player_pick: What the player has picked:
                1 = Rock, 2 = Paper, 3 = Scissors

        Returns:
            result: If AI or the player won or they tied:
                0 = Tie, 1 = AI Wins, 2 = Player Wins
        '''

        ai_pick = self.ai.pick()
        self.round += 1
        result = self.pick_winner(player_pick, ai_pick)
        self.ai.add_result(player_pick, ai_pick, result)
        return result


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
        if player_pick == 1 and ai_pick == 1:
            return 0
        if player_pick == 2 and ai_pick == 2:
            return 0
        if player_pick == 3 and ai_pick == 3:
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
ai = AI()
machine = RPS(ai)
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
    if result == 0:
        print("It's a tie!")
        ties += 1
    if result == 1:
        print("AI wins!")
        ai_wins += 1
    if result == 2:
        print("You win!")
        player_wins += 1
    
    print(f"Total: W:{player_wins} T:{ties} L:{ai_wins}")
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
