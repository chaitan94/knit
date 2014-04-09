import unittest,sys,os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from knit import main,bwt

class TestRle(unittest.TestCase):
	pass

class TestMtf(unittest.TestCase):
	pass

class TestBwt(unittest.TestCase):
	def testCyclicArray(self):
		self.failIf(bwt.getCyclicSuffixArray(list('s.t'))!=[['s','.','t'],['t','s','.'],['.','t','s']])
		self.failIf(bwt.getCyclicSuffixArray(list('sur'))!=[['s','u','r'],['r','s','u'],['u','r','s']])
	def testBwtEncode(self):
		self.failIf(bwt.encode('SIX.MIXED.PIXIES.SIFT.SIXTY.PIXIE.DUST.BOXES')[0]!='TEXYDST.E.IXIXIXXSSMPPS.B..E.S.EUSFXDIIOIIIT')
	def encodeDecode(self,string):
		compressedString = bwt.encode(string)
		reconstr = bwt.decode(compressedString)
		return string == reconstr
	def testBwt(self):
		self.failIf(not self.encodeDecode('sur'))
		self.failIf(not self.encodeDecode('SIX.MIXED.PIXIES.SIFT.SIXTY.PIXIE.DUST.BOXES'))

if __name__ == '__main__':
	unittest.main()
