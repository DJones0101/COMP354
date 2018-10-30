# Darius Jones
# test methods must start with "test"
# 10/29/2018

import unittest 
from lms import lms as l


class TestLms(unittest.TestCase):

	def setUp(self):
		pass

	def testCase1(self):
		self.assertEqual(l([4,6,5,9,1]), 3)

	def testCase2(self):
		self.assertEqual(l([15,27,14,38,26,55,46,65,85,]), 5)


if __name__ == "__main__":
	unittest.main()