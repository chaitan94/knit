def encode(byts):
	""" Run-Length-Encodes a byte array """
	n = len(byts)
	if n == 0: return
	b = byts[0]
	i = 1
	c = 1
	ret = []
	while i < n:
		if byts[i] == b and c < 255:
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
	ret = ''
	for x in rle:
		ret = ret + x[0]*x[1]
	return ret
