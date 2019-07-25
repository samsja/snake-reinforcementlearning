import numpy as np
import GameFolder.affichage as aff



class Game:

    def __init__(self, name,show = True, height=500,width=500):
        self.show = show
        self.screenHeight = height
        self.screenWidth = width
        self.name = name
        self.screen= 0
        self.screenInit = False
        if(self.show):
            self.__initScreen()

    def start(self):
        if(self.show):
            self.screen.start()

    def __del__(self):
        del self.screen
        aff.pygame.quit()
        print("destruction du Game : " + self.name)


#screen-------------------------------
    def __initScreen(self):
        aff.pygame.init()
        self.screen = aff.GameScreen(self.name,self.screenHeight,self.screenWidth)
        self.screenInit =True


    def screenSwitch(self):
        self.show = not(self.show)
        if(self.show and not(self.init)):
            self.__init()

class Snake(Game):
    def __init__(self, gridHeight=40,gridWidth=40  ,show = True, screenHeight=500,screenWidth=500):
        Game.__init__(self,"Snake",show,screenHeight,screenWidth)
        self.grid = [gridHeight,gridWidth]

        if(self.show):
            self.__initScreenSnake()


    def __initScreenSnake(self):

        self.screen.surface.fill((50,50,50))
        self.__drawGrid()



    def __drawGrid(self) :
        screen = self.screen.surface
        screenWidth = self.screenWidth
        screenHeight = self.screenHeight
        rows = self.grid[0]
        columns = self.grid[1]

        verticalSpaceBetween = screenWidth//columns
        horizontalSpaceBetween = screenHeight//rows
        x, y = 0, 0

        color =  (100,100,100)
        for _ in range(rows):
            x += verticalSpaceBetween
            aff.pygame.draw.line(screen, color, (x, 0),(x, screenWidth))
        for _ in range(columns) :
            y += horizontalSpaceBetween
            aff.pygame.draw.line(screen, color, (0, y),(screenHeight, y))

        aff.pygame.display.update()
        print("here")



    def start(self):
        Game.start(self)




def test():

    snake = Snake()
    snake.start()
