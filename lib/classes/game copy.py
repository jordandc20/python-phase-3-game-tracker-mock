from classes.result import Result

class Game:
    all=[]
    def __init__(self,title):
        if len(title)>0:
            self._title = title
            Game.all.append(self)

    @classmethod
    def get_all(cls):
        return cls.all
    
    def get_title(self):
        return self._title
        
    def set_title(self,title):
        pass    
    
    title = property( get_title, set_title)
    
    def results(self):
        all_results= Result.get_all()
        return [result for result in all_results if result.game==self]
    
    def players(self):
        return [result.player for result in self.results()]
    
    def average_score(self,player):
        games_played = player.num_times_played(self)
        total = sum([result.score for result in self.results() if result.player == player])

        return total/games_played


# from classes.result import Result

# class Game:
#     def __init__(self, title):
#         if len(title) > 0:
#             self._title = title
        
#     def get_title(self):
#         return self._title

#     def set_title(self, title):
#         pass
    
#     title = property(get_title, set_title)
    
#     def results(self):
#         all_results = Result.get_all()
#         return [result for result in all_results if result.game == self]
    

#     def players(self):
#         return [result.player for result in self.results()]
    
#     def average_score(self,player):       
#         total_plays = player.num_times_played(self)
#         total = sum([result.score for result in self.results() if result.player == player])
#         return total / total_plays
    
    