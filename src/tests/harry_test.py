import unittest

from main import main
from harry import Harry

class TestHarry(unittest.TestCase):
	def setUp(self):
		self.harry = Harry()
	def test_harry_doesnt_move_over_border_left(self):
		self.harry.x = 16
		self.harry.move_left()
		self.harry.move_left()
		self.harry.move_left()
		self.harry.move_left()
		self.assertEqueal((self.harry.x), 0)
