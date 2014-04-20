import heapq

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

if __name__ == "__main__":
	print decode(encode("chaitanya"))
