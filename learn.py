import Games.SnakeGame.game as snk
import Games.SnakeGame.screen as aff
from Games.GameScreen import pygame
from RL.DQN import DeepQNetwork as dqn

print("youpi learn")

game = snk.SnakeGame(rows = 7 , columns = 7)
