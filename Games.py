from meshok import Meshok
from Players import Player


class Game(object):
    def __init__(self):
        self.etap = 0
        self.gameOver = False
        self.m = Meshok()
        # p1=Player('Mary','Human')
        # p2=Player('lenovo','Comp')
        # p3 = Player('Borland', 'Cat')
        p1 = Player('Mary', 'Comp')
        p2 = Player('lenovo', 'Comp')
        p3 = Player('Borland', 'Comp')
        self.players = [p1, p3, p2]

    def show(self):
        print('Рaунд ', self.etap, '\n')
        for p in self.players:
            p.show()
        if self.gameOver:
            print('Игра закончена')

    def step(self):
        self.etap += 1
        b = self.m.get()
        print('Выпал боченок', b)
        # rez=[]
        for p in self.players:
            r = p.cross_out(b)
            if r == 'win':
                print('Выиграл', p.name)
                self.gameOver = True
            if r == 'loose':
                print('Проиграл', p.name)
                self.gameOver = True
            # rez.append(p.cross_out(b))
        # print (rez)
        # self.gameOver= self.m.isEmpty()
        if self.m.isEmpty():
            self.gameOver = True
