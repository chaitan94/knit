import struct

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

def encodeFile(infile, outfile):
	fi = open(infile,"rb").read()
	alph = list(set(fi))
	seq = encode(fi)

	fo = open(outfile, "wb")
	fo.write(struct.pack('i',len(seq)))
	for i in seq:
		fo.write(struct.pack('c', chr(i)))
	fo.write(struct.pack('i', len(alph)))
	fo.write(struct.pack('c'*len(alph), *alph))
	fo.close()

def decodeFile(infile, outfile):
	fi = open(infile,"rb")
	n = struct.unpack('i',fi.read(4))[0]
	seq = []
	for x in range(n):
		seq.append(ord(struct.unpack('c', fi.read(1))[0]))
	n = struct.unpack('i', fi.read(4))[0]
	alph = []
	for x in range(n):
		alph.append(struct.unpack('c', fi.read(1))[0])
	a = decode(seq, alph)
	
	fo = open(outfile, "wb")
	fo.write(a)
	fo.close()
