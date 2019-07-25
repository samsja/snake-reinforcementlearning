import contextlib
with contextlib.redirect_stdout(None): #this line is here to avoid the pygame message at every import pygame line comment this line if there is an issues witbh contextlib
    import pygame

class GameScreen:

    def __init__(self, name = "",screenWidth =100,screenHeight = 100):
        self.name = name
        print("init %s %d %d"%(self.name,screenWidth,screenHeight) )
        self.surface = pygame.display.set_mode((screenWidth, screenHeight))


        self.run = False

    def __del__(self):
        print("destruction du GameScreen : " + self.name )


    def start(self):
        self.run = True
        while(self.run):
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    self.end()

    def end(self):
        self.run = False




def test():
    a=0
    # pygame.init()
    #
    # screen1 = GameScreen("test",500,500)
    # screen1.start()
    # pygame.quit()
