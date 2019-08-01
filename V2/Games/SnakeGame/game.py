import Games.GameClass as gc
import random


class SnakeGame(gc.Game):
    def __init__(self, rows = 40,columns = 40):
        gc.Game.__init__(self,4)
        self.actions = ["up","down","rwit","left"]
        self.rows = rows
        self.columns = columns

        self.body = [[random.randint(0,self.rows),random.randint(0,self.columns)]]

        self.score = 0

        self.__addNewApple__()


    def __addNewApple__(self):
        x,y  = random.randint(0,self.rows),random.randint(0,self.columns)

        while ( [x,y] in self.body):
            x,y  = random.randint(0,self.rows),random.randint(0,self.columns)



    def move(self,action):
        gc.Game.move(self,action)

        if(self.actions[action] == "up"):
            mv = (0,-1)
        elif(self.actions[action] == "down"):
            mv = (0,1)
        elif(self.actions[action] == "left"):
            mv = (-1,0)
        elif(self.actions[action] == "rwit"):
            mv = (1,0)
        else:
            mv = (0,0)


        for i in range(len(self.body)):
            self.body[i][0] = (self.body[i][0] + mv[0])%self.columns
            self.body[i][1] = (self.body[i][1] + mv[1])%self.rows
