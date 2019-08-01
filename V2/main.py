import Games.SnakeGame.game as snk
import Games.SnakeGame.screen as aff

print("youpi")

a = snk.SnakeGame()

screen = aff.SnakeScreen(a)


input()

del(screen)
a.move(1)
