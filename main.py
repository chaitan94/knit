#!/usr/bin/python
import sys,time,struct,rle,mtf,cli

def recordTime(f):
	def w(*a):
		start = time.time()
		stop = time.time()
		f(*a)
		print("Completed in %f s" % (stop-start))
	return w

@recordTime
def compressFile(filename):
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
def decompress(filename):
	print("De-Compressing file %s" % filename)
	fi = open(filename,"rb").read()
	
	rlestr = struct.unpack('ci'*(len(fi)/8), fi)
	
	fo = open(filename[:-4]+".lulz","wb")
	fo.write(rle.decode(rlestr))
	fo.close()

@recordTime
def mtfcompress(filename):
	print("Compressing file %s.." % filename)
	fi = open(filename,"rb").read()
	inisize = len(fi)
	print("%d bytes read." % (inisize))
	alph = list(set(fi))
	seq = mtf.encode(fi)

	fo = open(filename+".mtf","wb")
	fo.write(struct.pack('i',len(seq)))
	fo.write(struct.pack('i'*len(seq), *seq))
	fo.write(struct.pack('i',len(alph)))
	fo.write(struct.pack('c'*len(alph), *alph))
	finsize = (2+len(seq))*4+len(alph)
	print("%d bytes written." % (finsize))
	print("%f%% Compressed." % ((1-(float(finsize)/inisize))*100))
	fo.close()

@recordTime
def mtfdecompress(filename):
	print("De-Compressing file %s" % filename)	
	fi = open(filename,"rb")
	n = struct.unpack('i',fi.read(4))[0]
	seq = []
	for x in range(n):
		seq.append(struct.unpack('i',fi.read(4))[0])
	n = struct.unpack('i',fi.read(4))[0]
	alph = []
	for x in range(n):
		alph.append(struct.unpack('c',fi.read(1))[0])
	a = mtf.decode(seq,alph)
	
	fo = open(filename[:-4]+".lulz","wb")
	fo.write(a)
	fo.close()

if __name__ == '__main__':
	if len(sys.argv) == 3:
		action = sys.argv[1]
		filename = sys.argv[2]

		if action == "compress":
			compressFile(filename)
		elif action == "decompress":
			decompress(filename)
		elif action == "mtfcompress":
			mtfcompress(filename)
		elif action == "mtfdecompress":
			mtfdecompress(filename)
		else:
			cli.usage()
	else:
		cli.usage()
