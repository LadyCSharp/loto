from meshok import Meshok
from Kard import Kards
import random

class TestMeshok:
    def test_init(self):
        m = Meshok()
        assert len(m.balls) == 90
        for i in range(1, 91):
            assert (i in m.balls) == True

    def test_get(self):
         m=Meshok()
         b=m.get()
         assert len(m.balls) == 89
         assert b>0
         assert b<=90

    def test_isempty(self):
         m=Meshok()
         assert m.isEmpty()==False

    def test_eq(self):
        m1=Meshok()
        m2=Meshok()
        assert (m1 == m2) == True
        b1 = m1.get()
        b2 = m2.get()
        if b1 == b2:
            assert (m1 == m2) == True
        else:
            assert (m1 != m2) == True

    def test_gt(self):
        m1=Meshok()
        m2=Meshok()
        assert (m1 > m2) == False
        b1 = m1.get()
        assert (m2 > m1) == True

    def test_ge(self):
        m1=Meshok()
        m2=Meshok()
        assert (m1 >= m2) == True
        b1 = m1.get()
        assert (m2 >= m1) == True

    def test_lt(self):
        m1=Meshok()
        m2=Meshok()
        assert (m1 < m2) == False
        b1 = m1.get()
        assert (m1 < m2) == True

    def test_contains(self):
        m = Meshok()
        for i in range(1,91):
            assert (i in m) == True
        for i in [0,100, -66]:
            assert (i in m) == False
    
class TestKard:
    def test_init(self):
        k=Kards()
        for i in range(3):
            for j in range(5):
                assert k.A[i,j]>=0
                assert k.A[i,j]<=90

    def test_isempty(self):
        k=Kards()
        assert k.isEmpty()==False

    def test_cross(self):
        k=Kards()
        k.cross_first()
        assert k.isEmpty()==False
        b=random.randint(1,90)
        if b in k:
            k.cross_out(b)
        assert k.isEmpty()==False

    def test_eq(self):
        m1=Kards()
        m2=Kards()
        assert (m1 == m2) == True
        b1 = m1.cross_first()
        b2 = m2.cross_first()
        if b1 == b2:
            assert (m1 == m2) == True
        else:
            assert (m1 != m2) == True

    def test_gt(self):
        m1 = Kards()
        m2 = Kards()
        assert (m1 > m2) == False
        b1 = m1.cross_first()
        assert (m2 > m1) == True

    def test_ge(self):
        m1 = Kards()
        m2 = Kards()
        assert (m1 >= m2) == True
        b1 = m1.cross_first()
        assert (m2 >= m1) == True

    def test_lt(self):
        m1 = Kards()
        m2 = Kards()
        assert (m1 < m2) == False
        b1 = m1.cross_first()
        assert (m1 < m2) == True

    def test_contains(self):
        m = Kards()
        for i in [150, 100, -66]:
            assert (i in m) == False