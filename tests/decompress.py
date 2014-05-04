import sys,os,subprocess
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from knit.__main__ import *

try:
	hfiles = subprocess.check_output('ls tests/*.h',shell=True).split()
	for i in hfiles:
		print "Decompressing file " + i + ".."
		decompress(i)
except Exception, e:
	print("No .h files available to decompress")
