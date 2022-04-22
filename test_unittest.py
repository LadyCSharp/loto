import unittest
import random
from Games import Game
from Players import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        print('Я выполняюсь до каждого теста')
        self.ph = Player('Mary', 'Human')
        self.pc = Player('Lenovo', 'Comp')
        self.p = Player('Borland', 'Cat')

    def tearDown(self):
        print('Я выполняюсь после каждого теста')
        del self.p
        del self.pc
        del self.ph

    def test_init(self):
        # p = Player('Mary', 'Human')
        self.assertEqual(self.p.name, 'Borland')
        self.assertEqual(self.p.typ, 'Cat')
        self.assertEqual(self.pc.name, 'Lenovo')
        self.assertEqual(self.pc.typ, 'Comp')
        self.assertEqual(self.ph.name, 'Mary')
        self.assertEqual(self.ph.typ, 'Human')
        
    def test_cross_out(self):
        # TODO: Прифигачить обезьянку
        # p = Player('Mary', 'Comp')
        b = random.randint(1, 90)
        self.assertEqual(self.pc.cross_out(b), 'continue')

    def test_eq(self):
        self.assertFalse(self.ph == self.p)
        self.assertFalse(self.ph == self.pc)
        self.assertFalse(self.pc == self.p)

    def test_str(self):
        self.assertIn('Человек', str(self.ph))
        self.assertIn('Компьютер', str(self.pc))
        self.assertIn('Котик', str(self.p))
        self.assertIn('Неведома зверушка по имени', str(Player('Нюся', 'Котеночек')))


class TestGame(unittest.TestCase):
    def test_init(self):
        g = Game()
        self.assertEqual(g.etap, 0)
        self.assertFalse(g.gameOver)
        self.assertEqual(len(g.players), 3)

    def test_step(self):
        g = Game()
        g.step()
        self.assertEqual(g.etap, 1)
        self.assertFalse(g.gameOver)
        self.assertEqual(len(g.players), 3)

    def test_str(self):
        g = Game()
        self.assertIn('Рaунд ', str(g))