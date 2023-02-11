import random
from Player import *

class Game:
    def __init__(self, player = Player("")):
        self.player = player
        self.chances = 10
        self.rounds = 1
        self.min_number = 1
        self.max_number = 100
        self.random_number = 1

    def draw_number(self):
        self.random_number = random.randint(self.min_number, self.max_number)

    def check_guess(self, player_guess):
        if player_guess == self.random_number:
            print(f"MESSAGE: {self.player.get_name()}, Congratulations, you have typed a correct number")
            self.player.add_score()
            self.chances = 0
            return True
        elif player_guess > self.random_number:
            self.chances -= 1
            print(f"MESSAGE: {self.player.get_name()}, Guess is bigger than drawn number, try again.")
            print(f"{self.chances} chances left.\n")
            return False
        else:
            self.chances -= 1
            print(f"MESSAGE: {self.player.get_name()}, Guess is lower than drawn number, try again.")
            print(f"{self.chances} chances left.\n")
            return False

    def start(self):
        chances = self.chances
        print("----- GAME START -----")
        print(f"Guess a number from range {self.min_number} to {self.max_number}")
        while self.rounds < 4:
            self.draw_number()
            print(f"\n*Round {self.rounds}\n")
            while self.chances > 0:
                guess = self.check_guess(self.player.enter_number(self.min_number, self.max_number))
                if not guess and self.chances == 0:
                    print("MESSAGE: Round is over, You didn't guess a number, let's start a next round")
            self.chances = chances
            self.rounds += 1
        
        print(f"MESSAGE: {self.player.get_name()}, score: {self.player.get_score()} in {self.rounds - 1} rounds.\n")
        print("----- GAME END -------")
