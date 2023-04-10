from classes.result import Result

class Game:
    def __init__(self, title):
        if len(title) > 0:
            self._title = title
        
    def get_title(self):
        return self._title

    def set_title(self, title):
        pass
    
    title = property(get_title, set_title)
    
    def results(self):
        all_results = Result.get_all()
        return [result for result in all_results if result.game == self]
    

    def players(self):
        return [result.player for result in self.results()]
    
    def average_score(self,player):       
        total_plays = player.num_times_played(self)
        total = sum([result.score for result in self.results() if result.player == player])
        return total / total_plays
    
    
    # Player num_times_played(game)
    # Returns the number of times the Player instance has played (Result instance created) the Game instance


    

# Game average_score(player)
    # Returns the average of all the player's scores for the Game instance
    # To average scores, add all result scores together for the player and divide by the total number of results for the player.
    
# Game results()
# Returns a list of all the Result instances for the Game.
# Game players()
# Returns a list of all of the Player instances that played the Game.
    
    
#     Game __init__(self, title)
# Game is initialized with a title (string)
# Title cannot be changed after the Game is initialized
# Game property title
    # Returns the Game's title
    # Titles must be strings greater than 0 characters