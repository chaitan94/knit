import unittest,sys,os,subprocess
sys.path.append('..')
from burrowsWheeler import main

class TestBwt(unittest.TestCase):
	def testOne(self):
		txtfiles = subprocess.check_output('ls tests/*.txt',shell=True).split()
		for i in txtfiles:
			main.compressFile(i)
		# self.failIf(1!=1)

if __name__ == '__main__':
	unittest.main()
