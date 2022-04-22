from Kard import Kards


class Player(object):
    def __init__(self, name, typ):
        self.name = name
        self.typ = typ
        self.k = Kards()

    def cross_out(self, ball):
        if self.typ == 'Comp':
            if ball in self.k:
                self.k.cross_out(ball)
                if self.k.isEmpty():
                    return 'win'
                else:
                    return 'continue'
        if self.typ == 'Human':
            q = input('зачеркивать?(Y/N)').lower()
            if q == 'y':
                if self.k.ball_in_kard(ball):
                    self.k.cross_out(ball)
                    if self.k.isEmpty():
                        return 'win'
                    else:
                        return 'continue'
                else:
                    return 'loose'

        if self.typ == 'Cat':
            q = input('зачеркивать?(Y/N)').lower()
            if q == 'y':
                if self.k.ball_in_kard(ball):
                    self.k.cross_out(ball)
                    if self.k.isEmpty():
                        return 'win'
                    else:
                        return 'continue'
                else:
                    self.k.cross_first()
                    if self.k.isEmpty():
                        return 'win'
                    else:
                        return 'continue'
        return 'continue'

    def __str__(self):
        if self.typ == 'Comp':
            s = "Компьютер по имени "

        elif self.typ == 'Human':
            s = "Человек по имени "

        elif self.typ == 'Cat':
            s = "Котик по имени "

        else:
            s = "Неведома зверушка по имени "
        s += self.name + '\n' + str(self.k)
        return s

    def __eq__(self, other):
        if isinstance(other, Player):
            return (self.typ == other.typ) and (self.k == other.k)
        else:
            return False
