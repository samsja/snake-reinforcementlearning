import contextlib
with contextlib.redirect_stdout(None): #this line is here to avoid the pygame message at every import pygame line comment this line if there is an issues witbh contextlib
    import pygame



class GameScreen:

    def __init__(self, name = "",screenWidth =100,screenHeight = 100):
        self.name = name
        print("init %s %d %d"%(self.name,screenWidth,screenHeight) )
        self.surface = pygame.display.set_mode((screenWidth, screenHeight))



        self.inRun = False

    def __del__(self):
        print("destruction du GameScreen : " + self.name )


    def run(self):
        self.inRun = True
        # while(self.inRun):
        #     for event in pygame.event.get() :
        #         if event.type == pygame.QUIT :
        #             self.inRun = False

        print("0")



def test():
    a=0
