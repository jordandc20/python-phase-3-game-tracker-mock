class Result:
    
    all =[]
    
    def __init__(self, player, game, score):
        if score >= 1 and score <=5000:
            self.player = player
            self.game = game
            self.score = score
            Result.all.append(self)
            
    @classmethod
    def get_all(cls):
        return cls.all
