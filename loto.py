
from Games import Game
if __name__ == '__main__':
  G = Game()
  G.show()
  while not G.gameOver:
    G.step()
    G.show()
 
