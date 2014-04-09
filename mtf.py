def encode(s):
	""" Transforms a given byte string to a Move-To-Front number sequence """
	alph = list(set(s))
	sequence = []
	for i in s:
		n = alph.index(i)
		sequence.append(n)
		while n > 0:
			alph[n] = alph[n-1]
			n = n - 1
		alph[0] = i
	return sequence

def decode(sequence,alph):
	string = ''
	for i in sequence:
		string = string + alph[i]
		c = alph[i]
		n = i
		while n > 0:
			alph[n] = alph[n-1]
			n = n - 1
		alph[0] = c
	return string
