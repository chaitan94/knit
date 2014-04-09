import unittest,sys,os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from knit import main

class TestRle(unittest.TestCase):
	pass

class TestMtf(unittest.TestCase):
	pass

class TestBwt(unittest.TestCase):
	pass

if __name__ == '__main__':
	unittest.main()
