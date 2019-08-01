
from Games.SnakeGame.game import SnakeGame

from Games.GameScreen import GameScreen

from Games.GameScreen import pygame

class SnakeScreen(GameScreen):

    def __init__(self, snake,name = "",screenWidth =500,screenHeight = 500, bottomColor = (0,50,50), gridThickness = 0):

        if(isinstance(gridThickness,float) or isinstance(gridThickness,int)):
            if( gridThickness < 0 or gridThickness > 1):
                raise Exception('argument errors','the gridThickness' + str(gridThickness) + " is not between 0 and 1")
        else:
            raise Exception('argument errors','the gridThickness' + str(gridThickness) + " is not an number")

        self.gridThickness = gridThickness


        GameScreen.__init__(self,snake,name,screenWidth,screenHeight,bottomColor)

        if(not(isinstance(snake,SnakeGame))):
            raise Exception('argument errors','the game' + str(snake) + " is not a snake game")



    def __initDisplay__(self):
        GameScreen.__initDisplay__(self)


        self.boxHeight = (self.screenHeight/self.game.rows) * (1-self.gridThickness/2)
        self.boxWidth = (self.screenWidth/self.game.columns) * (1-self.gridThickness/2)

        self.rowsHeight = (self.screenHeight/self.game.rows) * self.gridThickness
        self.columnsWidth = (self.screenWidth/self.game.columns) * self.gridThickness

        self.update()


    def __drawGrid__(self):
        color =  (0,100,0)
        x,y = -self.screenHeight/self.game.rows,-self.screenWidth/self.game.columns
        for _ in range(0,self.game.rows +1):
            x += self.screenWidth/self.game.rows
            pygame.draw.rect(self.surface, color, ( x - self.columnsWidth , 0 , 2*self.columnsWidth , self.screenWidth) )
        for _ in range(0,self.game.columns +1) :
            y += self.screenHeight/self.game.columns
            pygame.draw.rect(self.surface, color, ( 0,  y - self.rowsHeight , self.screenHeight, 2*self.rowsHeight) )

    def update(self):
        GameScreen.update(self)


        self.surface.fill(self.bottomColor)

        self.__drawGrid__()

        hx = self.screenHeight/self.game.rows
        hy = self.screenWidth/self.game.columns
        color = (0,100,0)

        for [x,y] in self.game.body:
            pygame.draw.rect(self.surface,color, ( x*hx + self.rowsHeight/2 , y*hy + self.columnsWidth/2, self.boxWidth,self.boxHeight ))

        pygame.display.update()

    def waitForInput(self):
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                action = -1
                return action

            elif event.type ==  pygame.KEYDOWN:
                if event.key ==  pygame.K_UP:
                    action = self.game.actions.index("up")
                elif event.key ==  pygame.K_DOWN:
                    action = self.game.actions.index("down")
                elif event.key ==  pygame.K_LEFT:
                    action = self.game.actions.index("left")
                elif event.key ==  pygame.K_RIGHT:
                    action = self.game.actions.index("rwit")

                return action

        return None
