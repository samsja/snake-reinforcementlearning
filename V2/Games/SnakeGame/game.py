import Games.GameClass as gc
import random


class SnakeGame(gc.Game):
    def __init__(self, rows = 40,columns = 40):
        gc.Game.__init__(self,4)
        self.actions = ["up","down","rwit","left"]
        self.rows = rows
        self.columns = columns

        self.body = [[ random.randint(0,self.rows),random.randint(0,self.columns)]]


    def move(self,action):
        gc.Game.move(self,action)
        print(self.actions[action])
