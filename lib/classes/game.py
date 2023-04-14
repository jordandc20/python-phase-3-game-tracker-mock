from classes.result import Result


class Game:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, input):
        if not hasattr(self, 'title') and type(input) == str and len(input) > 0:
            self._title = input
        # else:
        #     raise Exception('game title cannot be changed')

    def results(self):
        return [result for result in Result.get_results() if result.game == self]
    
    def players(self):
        return [result.player for result in self.results()]
    
    def average_score(self,player):
        if player in self.players():
            games_played = player.num_times_played(self)
            all_scores = [result.score for result in self.results() if result.player ==player] 
            return sum(all_scores) / games_played
        else:
            return 0