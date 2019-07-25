import numpy as np
import GameFolder.affichage as aff
import GameFolder.tools as t
import random



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
            self.screen.run()

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
        self.gridShape = [gridHeight,gridWidth]
        print("here")
        self.viper = t.snakeBody(self.gridShape[0],self.gridShape[1])
        self.viper.add(random.randint(0,gridHeight), random.randint(0,gridWidth))

        if(self.show):
            self.__initScreenSnake()



    def start(self):
        Game.start(self)

    def __initScreenSnake(self):

        self.screen.surface.fill((50,50,50))
        self.__show()


    def __show(self):
        self.__drawGrid()

        hx = self.screenWidth//self.gridShape[0]
        hy = self.screenHeight//self.gridShape[1]

        for st in self.viper.body:

            x = int(st[0])
            y = int(st[1])
            aff.pygame.draw.rect(self.screen.surface,
                (255,255,255),
                (x* hx,y* hy,hx,hy)
            )


        aff.pygame.display.update()



    def __drawGrid(self) :

        rows = self.gridShape[0]
        columns = self.gridShape[1]

        verticalSpaceBetween = self.screenWidth//columns
        horizontalSpaceBetween = self.screenHeight//rows
        x, y = 0, 0


        color =  (100,100,100)
        for _ in range(rows):
            x += verticalSpaceBetween
            aff.pygame.draw.line(self.screen.surface, color, (x, 0),(x, self.screenWidth))
        for _ in range(columns) :
            y += horizontalSpaceBetween
            aff.pygame.draw.line(self.screen.surface, color, (0, y),(self.screenHeight, y))










def test():

    snake = Snake()
    snake.start()

    while(snake.screen.inRun):
        for event in aff.pygame.event.get() :
            if event.type == aff.pygame.QUIT :
                snake.screen.inRun= False
            else:
                print(event.type)
