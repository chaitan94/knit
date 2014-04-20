import struct, heapq

class Node:
	def __init__(self):
		self.c = ''
		self.freq = 0
		self.left = None
		self.right = None
	def __lt__(self, other):
		return self.freq < other.freq
	def __eq__(self, other):
		return not self<other and not other<self
	def __ne__(self, other):
		return self<other or other<self
	def __gt__(self, other):
		return other<self
	def __ge__(self, other):
		return not self<other
	def __le__(self, other):
		return not other<self

def getHuffmanCodes(q):
	codes = {}
	path = []
	_getHuffmanCodes(q, path, codes)
	return codes

def _getHuffmanCodes(q, path, codes):
	if q is not None:
		if q.left is None and q.right is None:
			codes[q.c] = path
		_getHuffmanCodes(q.left, path + [False], codes)
		_getHuffmanCodes(q.right, path + [True], codes)

def getCounts(string):
	count = {}
	for i in string:
		if i in count:
			count[i] += 1
		else:
			count[i] = 1
	return count

def getHuffmanTree(count):
	n = len(count)
	q = []
	for i in count:
		a = Node()
		a.c = i
		a.freq = count[i]
		heapq.heappush(q, a)
	del count

	for i in xrange(n-1):
		z = Node()
		z.left = heapq.heappop(q)
		z.right = heapq.heappop(q)
		z.freq = z.left.freq + z.right.freq
		heapq.heappush(q,z)
	return q[0]

def encode(string):
	counts = getCounts(string)
	codes = getHuffmanCodes(getHuffmanTree(counts))
	bitarray = []
	for i in string:
		bitarray = bitarray + codes[i]
	return (counts, bitarray)

def decode((counts, bitarray)):
	q = getHuffmanTree(counts)
	p = q
	string = ''
	for i in bitarray:
		if i:
			p = p.right
		else:
			p = p.left
		if p.left is None and p.right is None:
			string += p.c
			p = q
	return string

def encodeFile(infile, outfile):
	fi = open(infile, "rb").read()
	counts, bitarray = encode(fi)
	fo = open(outfile, "wb")
	fo.write(struct.pack('i', len(counts)))
	for i in counts:
		fo.write(i)
		fo.write(struct.pack('i', counts[i]))
	n = len(bitarray)
	asds = 0
	for i in xrange(n/8):
		byt = 0
		for bb in xrange(8):
			bit = bitarray[8*i+bb]
			byt = byt << 1
			byt += bit
		fo.write(chr(byt))
	fo.close()

def decodeFile(infile, outfile):
	fi = open(infile,"rb")
	counts = {}
	nc = struct.unpack('i', fi.read(4))[0]
	for i in xrange(nc):
		char = fi.read(1)
		count = struct.unpack('i', fi.read(4))[0]
		counts[char] = count
	bitarray = []
	data = fi.read()
	for i in data:
		n = ord(i)
		minibitarray = []
		for j in xrange(8):
			minibitarray.append(n & 1 == True)
			n = n >> 1
		minibitarray.reverse()
		bitarray = bitarray + minibitarray
	fi.close()
	fo = open(outfile,"wb")
	decoded = decode((counts, bitarray))
	fo.write(decoded)
	fo.close()

if __name__ == "__main__":
	print decode(encode("chaitanya"))
