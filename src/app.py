from flask import Flask
import random

app = Flask(__name__)

# returns: 0 = Tie, 1 = AI Wins, 2 = Player Wins
# picks: 1 = Rock, 2 = Paper, 3 = Scissors

class RPS:
    def __init__(self):
        pass
    
    def change_pick(self, player_pick):
        self.player_pick = player_pick

    def calculate(self):
        self.ai_pick = random.randint(1, 3)

        #Ties:
        if self.player_pick == 1 and self.ai_pick == 1:
            return 0
        if self.player_pick == 2 and self.ai_pick == 2:
            return 0
        if self.player_pick == 3 and self.ai_pick == 3:
            return 0

        #AI wins:
        if self.player_pick == 1 and self.ai_pick == 2:
            return 1
        if self.player_pick == 2 and self.ai_pick == 3:
            return 1
        if self.player_pick == 3 and self.ai_pick == 1:
            return 1

        #AI wins:
        if self.player_pick == 1 and self.ai_pick == 3:
            return 2
        if self.player_pick == 2 and self.ai_pick == 1:
            return 2
        if self.player_pick == 3 and self.ai_pick == 2:
            return 2

machine = RPS()
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

    machine.change_pick(player_pick)
    result = machine.calculate()
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
@app.route("/")
def index():
    return "Heipparallaa!"
'''
