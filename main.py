import Games.SnakeGame.game as snk
import Games.SnakeGame.screen as aff
from Games.GameScreen import pygame



print("youpi")

game = snk.SnakeGame(rows = 10 , columns = 10)
screen = aff.SnakeScreen(game,screenWidth= 500,screenHeight=500,gridThickness=0)
action = 1

pygame.key.set_repeat(1,100)
while ( (action in game.getInputs()) or (action == -1) ):

    action = screen.waitForInput()
    if(action != None):
        reward = game.move(action)
        #print(reward)
        screen.update()
    else:
        action = -1


del(screen)
