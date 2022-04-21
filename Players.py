from Kard import Kards
class Player(object):
    def __init__(self,name,typ):
        self.name=name 
        self.typ=typ 
        self.k=Kards()

    def show(self):
        if self.typ=='Comp':
            print ("Компьютер по имени ", end='')

        elif self.typ=='Human':
            print ("Человек по имени ", end='')

        elif self.typ=='Cat':
            print ("Котик по имени ", end='')

        else:
            print ("Неведома зверушка по имени ", end='')
        print (self.name)
        self.k.show()

    def cross_out(self, ball):
        if self.typ=='Comp':
            if self.k.ball_in_kard(ball):
                self.k.cross_out(ball)
                if self.k.isEmpty():
                    return 'win'
                else:
                    return 'continue'
        if self.typ=='Human':
            q=input('зачеркивать?(Y/N)').lower()
            if q=='y':
                if self.k.ball_in_kard(ball):
                    self.k.cross_out(ball)
                    if self.k.isEmpty():
                        return 'win'
                    else:
                        return 'continue'
                else:
                    return 'loose'

        if self.typ=='Cat':
            q=input('зачеркивать?(Y/N)').lower()
            if q=='y':
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



