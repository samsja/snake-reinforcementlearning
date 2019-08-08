import Games.SnakeGame.game as snk
import Games.SnakeGame.screen as aff
from Games.GameScreen import pygame
from RL.DQN import DeepQNetwork as dqn



print("youpi")

game = snk.SnakeGame(rows = 7 , columns = 7)
screen = aff.SnakeScreen(game,screenWidth= 500,screenHeight=500,gridThickness=0)
action = 1

pygame.key.set_repeat(1,100)

clock = pygame.time.Clock()
while ( (action in game.getInputs()) or (action == -1) ):

    clock.tick(30)
    action = screen.waitForInput()
    if(action != None):
        reward = game.move(action)
        print(reward)
        screen.update()
    else:
        action = -1

del(screen)
