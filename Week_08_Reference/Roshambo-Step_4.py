import random
rps = ['Rock', 'Paper', 'Scissors']
active_players = []

class Player():
    def __init__(self, passed_name):
        self.player_name = passed_name
        self.player_score = 0
        active_players.append(self)
    def choose_rps(self):
        self.player_choice = random.choice(rps)
    def add_score(self):
        self.player_score += 1
