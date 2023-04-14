from classes.result import Result


class Player:
    all=[]
    def __init__(self, username):
        self.username = username
        Player.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, input):
        if type(input) == str and 2 <= len(input) <= 16:
            self._username = input
        # else:
        #     raise Exception('username must be a string between 2-16 chars ')

    def results(self):
        return [result for result in Result.get_results() if result.player == self]
    
    def games_played(self):
        return [result.game for result in self.results()]

    def played_game(self,game):
        return game in self.games_played()
    
    def num_times_played(self, game):
        return self.games_played().count(game)
    
    def add_result(self,game, score):
        Result(player=self, game=game, score=score)
        
    @classmethod 
    def highest_scored(cls,game):
        from .game import Game
        all_player_avg = []
        for player in cls.all:
            all_player_avg.append((player,Game.average_score(game,player)))
        return max(all_player_avg, key = lambda i : i[1])[0]
        
