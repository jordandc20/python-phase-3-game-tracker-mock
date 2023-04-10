class Result:
    
    all= []

    def __init__(self, player, game, score):
        if 1 <= score <= 5000:
            self.player = player
            self.game = game
            self.score = score
            Result.all.append(self)
            
    @classmethod
    def get_all(cls):
        return cls.all
            
    


# Result property player
    # Returns the player for the Result
    # Players must be Player instances
# Result property game
    # Returns the game that was played
    # Games must be Game instances


# Result __init__(self, player, game, score)
# Result is initialized with a Player instance, a Game instance, and a score (number)
# Result property score
# Returns the score for the Result instance
# Scores must be integers between 1 and 5000, inclusive