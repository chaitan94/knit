#!/usr/bin/python
import sys,time,struct,rle,mtf,bwt,cli

def recordTime(f):
	def w(*a):
		start = time.time()
		f(*a)
		stop = time.time()
		print("Completed in %f s" % (stop-start))
	return w

@recordTime
def compressFile(filename):
	pass

@recordTime
def decompress(filename):
	pass

@recordTime
def rlecompress(filename):
	print("Compressing file %s.." % filename)
	fi = open(filename,"rb").read()
	inisize = len(fi)
	print("%d bytes read." % (inisize))
	rledbytes = rle.encode(fi)

	fo = open(filename+".rle","wb")
	fo.write(struct.pack('ci'*len(rledbytes), *(item for t in rledbytes for item in t)))
	finsize = len(rledbytes)*8
	print("%d bytes written." % (finsize))
	print("%f%% Compressed." % ((1-(float(finsize)/inisize))*100))
	fo.close()

@recordTime
def rledecompress(filename):
	print("De-Compressing file %s" % filename)
	fi = open(filename,"rb").read()
	
	rlestr = struct.unpack('ci'*(len(fi)/8), fi)
	
	fo = open(filename[:-4]+".lulz","wb")
	fo.write(rle.decode(rlestr))
	fo.close()

@recordTime
def mtfencode(filename):
	print("Compressing file %s.." % filename)
	fi = open(filename,"rb").read()
	inisize = len(fi)
	print("%d bytes read." % (inisize))
	alph = list(set(fi))
	seq = mtf.encode(fi)

	fo = open(filename+".mtf","wb")
	fo.write(struct.pack('i',len(seq)))
	for i in seq:
		fo.write(struct.pack('c', chr(i)))
	fo.write(struct.pack('i',len(alph)))
	fo.write(struct.pack('c'*len(alph), *alph))
	finsize = (2+len(seq))+len(alph)
	print("%d bytes written." % (finsize))
	print("%f%% Compressed." % ((1-(float(finsize)/inisize))*100))
	fo.close()

@recordTime
def mtfdecode(filename):
	print("De-Compressing file %s" % filename)	
	fi = open(filename,"rb")
	n = struct.unpack('i',fi.read(4))[0]
	seq = []
	for x in range(n):
		seq.append(ord(struct.unpack('c',fi.read(1))[0]))
	n = struct.unpack('i',fi.read(4))[0]
	alph = []
	for x in range(n):
		alph.append(struct.unpack('c',fi.read(1))[0])
	a = mtf.decode(seq,alph)
	
	fo = open(filename[:-4]+".lulz","wb")
	fo.write(a)
	fo.close()

@recordTime
def bwtencode(filename):
	print("BWT-ing file %s" % filename)
	fi = open(filename,"rb").read()
	bwttransform = bwt.encode(fi)
	
	fo = open(filename+".bwt","wb")
	fo.write(struct.pack('i',bwttransform[0]))
	fo.write(struct.pack('c'*len(bwttransform[1]),*bwttransform[1]))
	fo.close()

@recordTime
def bwtdecode(filename):
	print("Reverse BWT-ing file %s" % filename)
	fi = open(filename,"rb")
	n = struct.unpack('i',fi.read(4))[0]
	c = fi.read()
	fi.close()
	fo = open(filename[:-4]+".lulz","wb")
	fo.write(bwt.decode((n,c)))
	fo.close()

if __name__ == '__main__':
	if len(sys.argv) == 3:
		action = sys.argv[1]
		filename = sys.argv[2]

		if action == "c":
			compressFile(filename)
		elif action == "d":
			decompress(filename)
		elif action == "rle":
			rlecompress(filename)
		elif action == "unrle":
			rledecompress(filename)
		elif action == "mtf":
			mtfencode(filename)
		elif action == "unmtf":
			mtfdecode(filename)
		elif action == "bwt":
			bwtencode(filename)
		elif action == "unbwt":
			bwtdecode(filename)
		else:
			cli.usage()
	else:
		cli.usage()
