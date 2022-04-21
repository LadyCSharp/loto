import random
class Meshok(object):
    """description of class"""
    def __init__(self) -> None:
        self.balls=[b for b in range(1,91)]


    def get(self):
        b=random.choice(self.balls)
        self.balls.remove(b)
        return b
    def isEmpty(self):
        return len(self.balls)==0