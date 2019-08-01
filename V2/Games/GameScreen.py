import contextlib
with contextlib.redirect_stdout(None): #this line is here to avoid the pygame message at every import pygame line comment this line if there is an issues witbh contextlib
    import pygame

from Games.GameClass import Game

class GameScreen:

    def __init__(self, game,name = "",screenWidth =500,screenHeight = 500,bottomColor = (0,50,50)):

        if( not(isinstance(screenWidth,int))):
            raise Exception('argument errors','the screenWidth ' + str(screenWidth) + " is not an integer")

        elif( not(isinstance(screenWidth,int))):
            raise Exception('argument errors','the screenHeight ' + str(screenHeight) + " is not an integer")

        elif( not(isinstance(name,str) )):
            raise Exception('argument errors','the name ' + str(name) + " is not a string")

        elif(not(isinstance(game,Game))):
            raise Exception('argument errors','the arguments' + str(game) + " is not a game")

        self.game = game
        pygame.init()

        self.surface = pygame.display.set_mode((screenWidth, screenHeight))

        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.bottomColor = bottomColor
        self.surface.fill(self.bottomColor)
        self.__initDisplay__()
        pygame.display.update()


    def __initDisplay__(self):
        return None

    def __del__(self):
        pygame.quit()

    def __str__(self):
        return "GameScreen " + str(id(self))
