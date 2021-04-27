import unittest
from src.harry import Harry
from src.main import main

#ilmoittaa import virhettä?
class TestHarry(unittest.TestCase):
    def setUp(self):
        self.harry = Harry()

    def test_harry_starts_from_right_position(self):
        self.harry.update()
        self.assertEqueal((self.harry.rect.x), 50)
        self.assertEqual((self.harry.rect.y), 50)
