from classes.result import Result

class Player:
    
    
    def __init__(self,username):
        if 2 <= len(username) <= 16:
            self.username=username
            
    def results(self):
        all_results = Result.get_all()
        return [result for result in all_results if result.player == self]

    def games_played(self):
        return [result.game for result in self.results()]
    #[game1 , game3 , game5, game3]
    
    def played_game(self, game):
        return game in self.games_played()
        # if game in self.games_played():
        #     return True
        # else:
        #     return False
    
    def num_times_played(self, game):
        # return len([game_played for game_played in self.games_played() if game_played == game])
        return self.games_played().count(game)
    # [game3,game3]
    
    def add_result(self, game, score):
        Result(self, game, score)
    
    
# Player played_game(game)
    # Returns True if the Player has played this Game (if there is a Result instance that has this Player and Game), returns False otherwise
    
# Player num_times_played(game)
    # Returns the number of times the Player instance has played (Result instance created) the Game instance

# Player add_result(game, score)
    # A Game instance and a score (number) are passed in as arguments
    # This method should create a new Result instance with that Player instance, Game instance, and score    
    
    
    
    
    
# Player
# Player results()
# Returns a list of Result instances associated with the Player instance.
# Player games_played()
# Returns a list of Game instances played by the Player instance.
    
    
    
# Player __init__(self, username)
# Player is initialized with a username (string)
# Usernames can be changed after the Player is initialized
# Player property username
# Returns the Player's username
# Usernames must be strings between 2 and 16 characters, inclusive
# if you are using exceptions comment out the test on lines 25 - 29 in the player_test.py and uncomment lines 37 - 44