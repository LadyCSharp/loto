
from Games import Game
if __name__ == '__main__':
  G = Game()
  print(G)
  while not G.gameOver:
    G.step()
    print(G)
 
