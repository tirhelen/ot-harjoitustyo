import unittest
from ..harry import Harry
from ..main import main
from ..level1 import Map


#ilmoittaa import virhettä?
class TestHarry(unittest.TestCase):
    def setUp(self):
        self.map = Map("level1..csv")
        self.harry = Harry({self.map})

    def test_harry_moves_to_right(self):
        self.harry.move_right()
        self.assertEqual((self.harry.rect.x), 60)
        self.assertEqual((self.harry.rect.y), 50)

    def test_harry_moves_to_left(self):
        self.harry.rect.x = 100
        self.harry.move_left()
        self.assertEqual((self.harry.rect.x), 40)
        self.assertEqual((self.harry.rect.y), 50)
