import random


class Meshok(object):
    """description of class"""
    def __init__(self) -> None:
        self.balls = [b for b in range(1,91)]

    def get(self):
        b = random.choice(self.balls)
        self.balls.remove(b)
        return b
    def isEmpty(self):
        return len(self.balls) == 0

    def __str__(self):
        return "В мешочке " + str(len(self.balls)) + " бочонков"

    def __eq__(self, other):
        if isinstance(other, Meshok):
            return self.balls == other.balls
        else:
            return False

    def __contains__(self, item):
        return item in self.balls

    def __gt__(self, other):
        # По количесту боченков
        return len(self) > len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __len__(self):
        return len(self.balls)