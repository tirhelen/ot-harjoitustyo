import unittest
from ..harry import Harry
from ..main import main
from ..level1 import Map


#ilmoittaa import virhettä?
class TestHarry(unittest.TestCase):
    def setUp(self):
        self.map = Map("level1..csv")
        self.harry = Harry({self.map})

    def test_harry_starts_from_right_position(self):
        self.harry.update()
        self.assertEqual((self.harry.rect.x), 50)
        self.assertEqual((self.harry.rect.y), 50)
