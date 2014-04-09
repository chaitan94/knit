import sys,os,subprocess
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from knit import main

txtfiles = subprocess.check_output('ls tests/*.txt',shell=True).split()
for i in txtfiles:
	main.compressFile(i)
