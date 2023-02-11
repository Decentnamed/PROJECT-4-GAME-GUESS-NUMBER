# Simply game with guess number

from Player import *
from Game import *

player = Player("Dawid")
game = Game(player)

if __name__ == "__main__":
    game.start()
