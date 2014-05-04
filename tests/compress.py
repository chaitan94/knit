import sys, os, subprocess
from os.path import isfile, join
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from knit.__main__ import *

testsdir = "tests/"

try:
	txtfiles = [ testsdir + f for f in os.listdir(testsdir) if isfile(join(testsdir, f)) ]
	txtfiles = filter(lambda x: x[-4:] == ".txt", txtfiles)
	for i in txtfiles:
		print "Compressing file " + i + ".."
		compress(i)
except Exception, e:
	print("No .txt files available to compress")
