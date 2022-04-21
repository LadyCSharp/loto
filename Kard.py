import random
import numpy as np
from numpy.core.fromnumeric import shape
class Kards(object):
    """description of class"""
    def __init__(self):
        self.A = np.zeros(shape=(3,9),dtype='int')
        balls=[b for b in range(1,91)]
        for i in range(3):
            for j in range(5):
                pos=random.randint(0,8)
                if self.A[i,pos]==0:
                       b=random.choice(balls)
                       balls.remove(b)
                       self.A[i,pos]=b
                else:
                    while True:
                        pos=random.randint(0,8)
                        if self.A[i,pos]==0:
                           b=random.choice(balls)
                           balls.remove(b)
                           self.A[i,pos]=b
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
        for i in range(3):
            for j in range(9):
                if (self.A[i,j]!=0) and (self.A[i,j]!=150):
                    return False
        return True

    def cross_out(self, ball):
        for i in range(3):
            for j in range(9):
                if self.A[i,j]==ball:
                    self.A[i,j]=150
        

    def ball_in_kard(self, ball):
        return ball in self.A

    def cross_first(self):
        for i in range(3):
            for j in range(9):
                if (self.A[i,j]!=0) and (self.A[i,j]!=150):
                    self.A[i,j]=150
                    return