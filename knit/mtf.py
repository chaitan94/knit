import struct

def encode(string):
	""" Transforms a given byte string to a Move-To-Front number sequence """
	alph = list(set(string))
	orgalph = alph[:]
	sequence = []
	for i in string:
		n = alph.index(i)
		sequence.append(n)
		while n > 0:
			alph[n] = alph[n-1]
			n = n - 1
		alph[0] = i
	return (sequence, orgalph)

def decode(sequence, alph):
	string = ''
	for i in range(len(sequence)):
		string = string + alph[sequence[i]]
		c = alph[sequence[i]]
		n = sequence[i]
		while n > 0:
			alph[n] = alph[n-1]
			n = n - 1
		alph[0] = c
	return string

def encodeFile(infile, outfile):
	fi = open(infile,"rb").read()
	seq, alph = encode(fi)

	fo = open(outfile, "wb")
	fo.write(struct.pack('i',len(seq)))
	for i in seq:
		fo.write(struct.pack('c', chr(i)))
	fo.write(struct.pack('i', len(alph)))
	fo.write(struct.pack('c'*len(alph), *alph))
	fo.close()

def decodeFile(infile, outfile):
	fi = open(infile,"rb")
	n = struct.unpack('i', fi.read(4))[0]
	seq = []
	for x in range(n):
		seq.append(ord(fi.read(1)))
	n = struct.unpack('i', fi.read(4))[0]
	alph = []
	for x in range(n):
		alph.append(fi.read(1))
	a = decode(seq, alph)
	
	fo = open(outfile, "wb")
	fo.write(a)
	fo.close()
