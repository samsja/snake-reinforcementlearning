import Games.SnakeGame.game as snk
import Games.SnakeGame.screen as aff

print("youpi")

game = snk.SnakeGame()

screen = aff.SnakeScreen(game,screenWidth= 750,screenHeight=750,gridThickness=0)

action = 1

while ( (action in game.getInputs()) or (action == -1) ):

    action = screen.waitForInput()
    if(action != None):
        game.move(action)
        screen.update()
    else:
        action = -1


del(screen)
