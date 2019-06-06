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


def playGame(player_1, player_2):
    player_1.choose_rps()
    player_2.choose_rps()
    winner = 0
    winner_name = 'Neither'

    p1_choice = player_1.player_choice
    p2_choice = player_2.player_choice

    if p1_choice == 'Rock':
        if p2_choice == 'Rock':
            winner = 0
        elif p2_choice == 'Paper':
            winner = 2
        else:
            winner = 1
    elif p1_choice == 'Paper':
        if p2_choice == 'Paper':
            winner = 0
        elif p2_choice == 'Scissors':
            winner = 2
        else:
            winner = 1
    else:
        if p2_choice == 'Scissors':
            winner = 0
        elif p2_choice == 'Rock':
            winner = 2
        else:
            winner = 1

    if winner == 1:
        player_1.add_score()
        winner_name = player_1.player_name
    if winner == 2:
        player_2.add_score()
        winner_name = player_2.player_name

    display_string = '%s chose %s, and %s chose %s. %s wins!' % (player_1.player_name, p1_choice, player_2.player_name, p2_choice, winner_name)
    print(display_string)
