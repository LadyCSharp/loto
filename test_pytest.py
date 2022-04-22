from meshok import Meshok
from Kard import Kards
import random
class TestMeshok:
    def test_init(self):
        m=Meshok()
        assert len(m.balls) == 90
        for i in range(1,91):
            assert (i in m.balls)==True

    def test_get(self):
         m=Meshok()
         b=m.get()
         assert len(m.balls) == 89
         assert b>0
         assert b<=90

    def test_isempty(self):
         m=Meshok()
         assert m.isEmpty()==False
    
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
        if k.ball_in_kard(b):
            k.cross_out(b)
        assert k.isEmpty()==False

