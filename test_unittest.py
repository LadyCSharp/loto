import unittest
import random
from Games import Game
from Players import Player


class TestPlayer(unittest.TestCase):
     
    def test_init(self):
        p = Player('Mary', 'Human')
        self.assertEqual(p.name, 'Mary')
        self.assertEqual(p.typ, 'Human')
        
    def test_cross_out(self):
        # TODO Прифигачить обезьянку
        p = Player('Mary', 'Comp')
        b = random.randint(1, 90)
        self.assertEqual(p.cross_out(b), 'continue')


class TestGame(unittest.TestCase):
    def test_init(self):
        g = Game()
        self.assertEqual(g.etap, 0)
        self.assertFalse(g.gameOver)
        self.assertEqual(len(g.players), 3)