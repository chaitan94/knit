import struct

def encode(string):
	strlist = list(string)
	cyclicSuffixArray = getCyclicSuffixArray(strlist)
	sortedSuffixArray = sorted(cyclicSuffixArray)
	transform = []
	n = sortedSuffixArray.index(strlist)
	for i in sortedSuffixArray:
		transform.append(i[-1])
	return (n,''.join(transform))

def decode(transform):
	string = transform[1]
	n = len(string)
	table = [[]]*n
	for x in xrange(n):
		for y in xrange(n):
			table[y] = list(string[y]) + table[y]
		table = sorted(table)
	return ''.join(table[transform[0]])

def getCyclicSuffixArray(strlist):
	cyclicSuffixArray = []
	strlen = len(strlist)
	for i in xrange(strlen):
		cyclicSuffixArray.append(strlist[(strlen-i):]+strlist[:(strlen-i)])
	return cyclicSuffixArray

def encodeFile(infile, outfile):
	fi = open(infile, "rb").read()
	bwttransform = encode(fi)
	fo = open(outfile, "wb")
	fo.write(struct.pack('i', bwttransform[0]))
	fo.write(struct.pack('c'*len(bwttransform[1]), *bwttransform[1]))
	fo.close()

def decodeFile(infile, outfile):
	fi = open(infile,"rb")
	n = struct.unpack('i',fi.read(4))[0]
	c = fi.read()
	fi.close()
	fo = open(outfile,"wb")
	fo.write(decode((n,c)))
	fo.close()
