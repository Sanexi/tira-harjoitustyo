'''Imports:
    random: Used for round 1 random pick.'''
import random


class Models:
    '''Class that holds models based on a distinct Markov chain algorithm.'''

    def __init__(self, memory):
        '''Model constructor

        Args:
            memory: List of previous rounds and their results.
            Used to make the models choose their picks.'''

        self.memory = memory

    def model_0(self):
        '''Model 0: Chooses what would've lost to player's previous choice.'''
        last = self.memory.get_result()
        if len(last) == 0:
            m0_pick = random.randint(1, 3)
            return m0_pick
        m0_pick = last[-1][0]
        if m0_pick == 1:
            m0_pick += 2
            return m0_pick
        m0_pick -= 1
        return m0_pick

    def model_1(self):
        '''Model 1: Chooses what would've won player's previous choice.'''
        last = self.memory.get_result()
        m1_pick = last[-1][0]
        if m1_pick == 3:
            m1_pick = 1
            return m1_pick
        m1_pick += 1
        return m1_pick

    def model_2(self):
        '''Model 2: Chooses what would've tied with player's previous choice.'''
        last = self.memory.get_result()
        m2_pick = last[-1][0]
        return m2_pick

    def model_3(self):
        '''Model 3: A Vector model. Player plays in certain pattern (uses a vector)
        ie. rock>paper>scissors or rock>scissors>paper.'''

        last = self.memory.get_result()
        if len(last) >= 2:
            # If vector = 1
            if last[-2][0] == 3 and last[-1][0] == 1:
                m3_pick = 3
                return m3_pick
            if last[-2][0] != 3 and last[-1][0] == last[-2][0]+1:
                m3_pick = last[-1][0]-1
                return m3_pick

            # If vector = 2
            if last[-2][0] == 1 and last[-1][0] == 3:
                m3_pick = 3
                return m3_pick
            if last[-2][0] != 1 and last[-1][0] == last[-2][0]-1:
                m3_pick = last[-1][0]
                return m3_pick

        # If no vector
        if last[-1][0] == 1:
            m3_pick = 3
            return m3_pick
        m3_pick = last[-1][0]-1
        return m3_pick

    def model_4(self):
        '''Model 4: Frequency model. Player tends to pick the same pick most of the time.'''
        last = self.memory.get_result()
        player_picks = []
        for i in last:
            player_picks.append(i[0])
        most_freq = max(player_picks, key=player_picks.count)
        if most_freq == 3:
            m4_pick = 1
        else:
            m4_pick = most_freq + 1
        return m4_pick

    def model_5(self):
        '''Model 5: Least frequent model. Player tends to picks the least frequent pick.'''
        last = self.memory.get_result()
        player_picks = []

        for i in last:
            player_picks.append(i[0])
        if 1 not in player_picks:
            least_freq = 1
        elif 2 not in player_picks:
            least_freq = 2
        elif 3 not in player_picks:
            least_freq = 3
        else:
            least_freq = min(player_picks, key=player_picks.count)

        if least_freq == 3:
            m5_pick = 1
        else:
            m5_pick = least_freq + 1
        return m5_pick

    #TODO: Model 6: Model to detect patterns in the last 6 rounds (mainly 3+3 rounds played in the same way).

    def get_models(self):
        '''Returns all modelpicks to the Ensembler'''
        last = self.memory.get_result()
        m0_pick = self.model_0()
        if len(last) == 0:
            return [m0_pick]
        m1_pick = self.model_1()
        m2_pick = self.model_2()
        m3_pick = self.model_3()
        m4_pick = self.model_4()
        m5_pick = self.model_5()
        return (m0_pick, m1_pick, m2_pick, m3_pick, m4_pick, m5_pick)


class Ensembler:
    '''Ensembler chooses the best model for all situations.'''

    def __init__(self, models):
        '''Ensembler constructor

        Args:
            models: class that holds different models for the Ensembler to decide which to use.'''

        self.models = models
        self.round = 0

        # Model scores:
        self.scores = []

    def pick(self):
        '''Decides which model the Ensembler should pick.
        First round plays random, otherwise checks the scores of different models.
        If many max scores, pick the highest picked.

        Returns:
            Ensembler's pick
        '''
        model_pick = self.models.get_models()
        if self.round == 0:
            pick = model_pick[0]
        else:
            scores = self.get_score()

            #Checking if all max scoring models agree on the pick
            occurrences = lambda s, lst: (i for i,e in enumerate(lst) if e == s)
            indexes = list(occurrences(max(scores), scores))
            counter = 0
            best_picks = []
            for i in indexes:
                best_picks.append(model_pick[i])
            for i in indexes:
                freq = best_picks.count(model_pick[i])
                if freq > counter:
                    counter = freq
                    model = i
            print("Model used", model)
            pick = model_pick[model]

        self.round += 1
        return pick

    def add_score(self, player_pick):
        '''Keeps scoring for every model, ensembler uses the scores to play against the player.
        Gives score to all models depending on if they choose wrong or right.
        Only keeps score for the last 5 rounds.

        Args:
            player_pick: What player picked this round. Compares this to models' picks.
        '''

        this_round = [0, 0, 0, 0, 0, 0]
        model_pick = self.models.get_models()
        if player_pick == 3:
            correct_pick = 1
        else:
            correct_pick = player_pick + 1

        ind = 0
        for i in model_pick:
            if i == correct_pick:
                this_round[ind] += 1
            elif i not in (correct_pick, player_pick):
                this_round[ind] -= 1
            ind += 1

        if len(self.scores) == 6:
            self.scores.pop(0)
        self.scores.append(this_round)

    def get_score(self):
        '''Returns:
            Score in usable form, adds up score from all rounds'''

        m0_score = 0
        m1_score = 0
        m2_score = 0
        m3_score = 0
        m4_score = 0
        m5_score = 0
        for i in self.scores:
            m0_score += i[0]
            m1_score += i[1]
            m2_score += i[2]
            m3_score += i[3]
            m4_score += i[4]
            m5_score += i[5]
        return [m0_score, m1_score, m2_score, m3_score, m4_score, m5_score]


class Memory:
    '''Memory to remember earlier rounds.'''

    def __init__(self):
        self.prev_rounds = []

    def add_result(self, player_pick, ai_pick, result):
        '''Adds a result to memory for later use and learning.
        Memory is kept only 5 rounds long, later rounds will be removed.
        Picks are stored as a number value:
            1 = Rock, 2 = Paper, 3 = Scissors
        Results are stored in numbers as well:
            0 = Tie, 1 = AI Wins, 2 = Player Wins
        '''

        if len(self.prev_rounds) == 5:
            self.prev_rounds.pop(0)
        self.prev_rounds.append((player_pick, ai_pick, result))

    def get_result(self):
        '''Returns:
            self.prev_rounds: results of previous rounds'''
        return self.prev_rounds


class RPS:
    '''Creates the fountation for the game.'''

    def __init__(self, ensembler, memory):
        '''Rock-paper-scissors gameconstructor

        Args:
            ai: Ensembler that will use the right model to defeat the player.
            memory: class to store previous rounds.'''

        self.ensembler = ensembler
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

        ai_pick = self.ensembler.pick()
        result = self.pick_winner(player_pick, ai_pick)

        if self.round != 0:
            self.ensembler.add_score(player_pick)
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
        # Ties:
        if player_pick == ai_pick:
            return 0
        # AI wins:
        if player_pick == 3 and ai_pick == 1 or player_pick == ai_pick-1:
            return 1
        # AI wins:
        if player_pick == 1 and ai_pick == 3 or player_pick == ai_pick+1:
            return 2


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
    print(ensembler.get_score())
    print(ai.get_models())
    print("")