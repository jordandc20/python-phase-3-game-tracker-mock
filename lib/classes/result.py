class Result:
    all=[]
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)
        
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self,input):
        if isinstance(input, (int,float)) and 1<= input <= 5_000:
            self._score = input 
            
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self,input):
        from .player import Player
        if isinstance(input, Player):
            self._player = input 
            
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self,input):
        from .game import Game
        if isinstance(input, Game):
            self._game = input 

    @classmethod
    def get_results(cls):
        return cls.all