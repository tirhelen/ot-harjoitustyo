import unittest
from src.harry import Harry
from src.main import main


class TestHarry(unittest.TestCase):
    def setUp(self):
        self.harry = Harry()

    def test_harry_doesnt_move_over_border_left(self):
        self.harry.update()
        self.assertEqueal((self.harry.rect.x), 50)
