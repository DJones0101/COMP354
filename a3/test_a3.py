#!/usr/bin/env python3

# Darius Jones
# 10/31/2018
# COMP 354
# Python 3.6

import unittest
from a3 import shuffle as a

class TestA3(unittest.TestCase):

	def test_case1(self):
		self.assertEqual(a("01101110","10101000","0110110011101000"), "Yes")

	def test_case2(self):
		self.assertEqual(a("000","111","010101"), "Yes")
	
	def test_case3(self):
		self.assertEqual(a("011","011","001111"), "Yes")

	def test_case4(self):
		self.assertEqual(a("10","0101","001111"), "No")

if __name__ == "__main__":
	unittest.main()

    