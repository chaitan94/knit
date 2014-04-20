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
	codes = []
	path = []
	_getHuffmanCodes(q, path, codes)
	return codes

def _getHuffmanCodes(q, path, codes):
	if q is not None:
		if q.left is None and q.right is None:
			codes.append((q.c, path))
		_getHuffmanCodes(q.left, path + [False], codes)
		_getHuffmanCodes(q.right, path + [True], codes)

def encode(string):
	count = {}
	for i in string:
		if i in count:
			count[i] += 1
		else:
			count[i] = 1
	del string

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
	return getHuffmanCodes(q[0])

if __name__ == "__main__":
	print encode("chaitanya")
