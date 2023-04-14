#!/usr/bin/env python3
import ipdb

from classes.player import Player
from classes.game import Game
from classes.result import Result

if __name__ == '__main__':
    game = Game("Skribbl.io")
    game_2 = Game("Scattegories")
    player = Player('Saaammmm')
    player_2 = Player('ActuallyTopher')
    Result(player, game, 2000)
    Result(player, game_2, 19)
    Result(player, game, 1900)
    Result(player_2, game_2, 9)

    ipdb.set_trace()
