import random
import numpy as np


class Kards(object):
    """description of class"""
    def __init__(self):
        self.A = np.zeros(shape=(3, 9), dtype='int')
        balls = [b for b in range(1, 91)]
        for i in range(3):
            for j in range(5):
                pos = random.randint(0, 8)
                if self.A[i, pos] == 0:
                    b = random.choice(balls)
                    balls.remove(b)
                    self.A[i, pos] = b
                else:
                    while True:
                        pos = random.randint(0,8)
                        if self.A[i, pos] == 0:
                           b = random.choice(balls)
                           balls.remove(b)
                           self.A[i, pos] = b
                           break

    def show(self):
        #print(self.A)
          for i in range(3):
            for j in range(9):
                if self.A[i,j]==0:
                    print('  ', end='')
                elif self.A[i,j]==150:
                    print('--', end='')
                else:
                    print("{:2d}".format(self.A[i,j]), end='')
                print(' | ', end='')
            print()

    def isEmpty(self):
        return len(self) == 0

    def cross_out(self, ball):
        for i in range(3):
            for j in range(9):
                if self.A[i,j]==ball:
                    self.A[i,j]=150
        

    #def ball_in_kard(self, ball):
        #return ball in self.A

    def cross_first(self):
        for i in range(3):
            for j in range(9):
                if (self.A[i,j]!=0) and (self.A[i,j]!=150):
                    self.A[i,j]=150
                    return

    def __str__(self):
        s=""
        for i in range(3):
            for j in range(9):
                if self.A[i, j] == 0:
                    s += '  '
                elif self.A[i, j] == 150:
                    s += '--'
                else:
                    s += "{:2d}".format(self.A[i, j])
                s += ' | '
            s += '\n'
        return s

    def __len__(self):
        l = 0

        for i in range(3):
            for j in range(9):
                if (self.A[i, j] != 0) and (self.A[i, j] != 150):
                    l += 1
        return l

    def __eq__(self, other):
        if isinstance(other, Kards):
            if len(self) == len(other):
                return True
        return False

    def __gt__(self, other):
        return len(self) > len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __contains__(self, item):
        return item in self.A