
from Games.SnakeGame.game import SnakeGame

from Games.GameScreen import GameScreen

from Games.GameScreen import pygame

class SnakeScreen(GameScreen):

    def __init__(self, snake,name = "",screenWidth =500,screenHeight = 500,bottomColor = (0,50,50), gridThickness = 0.2):
        GameScreen.__init__(self,snake,name,screenWidth,screenHeight,bottomColor)

        if(not(isinstance(snake,SnakeGame))):
            raise Exception('argument errors','the game' + str(snake) + " is not a snake game")

        if(isinstance(gridThickness,float) or isinstance(gridThickness,int)):
            if( gridThickness < 0 or gridThickness > 1):
                raise Exception('argument errors','the gridThickness' + str(gridThickness) + " is not between 0 and 1")
        else:
            raise Exception('argument errors','the gridThickness' + str(gridThickness) + " is not an number")


        self.boxHeight = (self.screenHeight/self.game.rows) * (1-gridThickness)
        self.boxWidth = (self.screenWidth/self.game.columns) * (1-gridThickness)


    def __initDisplay__(self):
        GameScreen.__initDisplay__(self)
        self.__drawGrid__()

    def __drawGrid__(self):
        print(" draw grid")
