def encode(byts):
	""" Run-Length-Encodes a byte array """
	n = len(byts)
	if n == 0: return
	b = byts[0]
	i = 1
	c = 1
	ret = []
	while i < n:
		if byts[i] == b:
			c = c + 1
		else:
			ret.append((b,c))
			b = byts[i]
			c = 1
		i = i + 1
	ret.append((b,c))
	return ret

def decode(rle):
	""" Decodes a Run-Length-Encoded byte array """
	n = len(rle)/2
	ret = ''
	for x in xrange(n):
		ret = ret + rle[x*2]*int(rle[x*2+1])
	return ret
