import Games.GameClass as gc
import random
import math


class SnakeGame(gc.Game):
    def __init__(self, rows = 40,columns = 40):
        gc.Game.__init__(self,4)

        if( not(isinstance(rows,int))):
            raise Exception('argument errors','the screenWidth ' + str(rows) + " is not an integer")

        if( not(isinstance(columns,int))):
            raise Exception('argument errors','the screenHeight ' + str(columns) + " is not an integer")

        self.actions = ["up","down","rwit","left"]
        self.rows = rows
        self.columns = columns

        self.body = [[random.randint(0,self.rows),random.randint(0,self.columns)]]

        self.score = 0

        self.__addNewApple__()




    def __addNewApple__(self):
        x,y  = random.randint(0,self.rows-1),random.randint(0,self.columns-1)

        while ( [x,y] in self.body):
            x,y  = random.randint(0,self.rows-1),random.randint(0,self.columns-1)

        self.applePos = [x,y]

    def __verifyApple__(self):
        for  [x,y] in self.body :
            if( [x,y] == self.applePos):
                return True
        return False



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

        x = (self.body[0][0] + mv[0])%self.columns
        y = (self.body[0][1] + mv[1])%self.rows

        self.body.insert(0,[x,y])

        rewardDeath = -500*self.rows*self.columns
        rewardNone = -50
        rewardEat = 100


        if( len(self.body)>3):
            if( [x,y] in self.body[1:-1]):
                self.__init__(self.rows,self.columns)
                return rewardDeath
        elif( [x,y] in self.body[1:len(self.body)]):
            self.__init__(self.rows,self.columns)
            return rewardDeath

        if( not(self.__verifyApple__()) ) :
            self.body.pop(-1)
            return rewardNone
        else:
            self.__addNewApple__()
            self.score = self.score +1
            return max(rewardEat * (1 + math.pow((self.score)/2,1.25)),rewardDeath/10)

        return 0
