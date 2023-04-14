from classes.result import Result
from classes.game import Game

class Player:
    def __init__(self,username):
        if len(username) >= 2 and len(username) <= 16:
            self.username = username
            
    def results(self):
        all_results= Result.get_all()
        return [result for result in all_results if result.player==self]

    def games_played(self):
        return [result.game for result in self.results()]
    
    def add_result(self,game, score):
        Result(self,game, score)
    
    def num_times_played(self,game):
        return len([game_played for game_played in self.games_played() if game_played ==game])
    
    def played_game(self,game):
        return game in self.games_played()
    
#     from classes.result import Result

# class Player:
    
    
#     def __init__(self,username):
#         if 2 <= len(username) <= 16:
#             self.username=username
            
#     def results(self):
#         all_results = Result.get_all()
#         return [result for result in all_results if result.player == self]

#     def games_played(self):
#         return [result.game for result in self.results()]
#     #[game1 , game3 , game5, game3]
    
#     def played_game(self, game):
#         return game in self.games_played()
#         # if game in self.games_played():
#         #     return True
#         # else:
#         #     return False
    
#     def num_times_played(self, game):
#         # return len([game_played for game_played in self.games_played() if game_played == game])
#         return self.games_played().count(game)
#     # [game3,game3]
    
#     def add_result(self, game, score):
#         Result(self, game, score)