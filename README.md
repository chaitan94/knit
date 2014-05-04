knit
===============

knit is a simple file compressor using Burrows-Wheeler Transform (BWT) and then finally compressed by the Run Length Encoding (RLE) and Move to Front Transform (MFT) techniques.

## Instructions

Run pre written tests:
 * Open a terminal in root folder of the project
 * run `python tests/compress.py`
 * This will compress all .txt files present in tests folder
 * run `python tests/decompress.py`
 * This will decompress all .h files present in tests folder (Note: Decompression may take some time)

Cleaning .h and .lulz files:
 * run `python tests/clean.py`
 * This will delete all .h and .lulz files present in tests folder

To test it manually:
 * Open a terminal in root folder of the project
 * put a text file you want to compress in tests folder
 * run `python knit compress tests/filename.txt`
 * run `python knit decompress tests/filename.txt.h`

## Project Structure
knit folder contains code for BWT, MTF, RLE and huffman in python
	bwt.py file has code for coding and decoding in BWT
	mtf.py file has code for coding and decoding in MTF
	rle.py file has code for coding and decoding in RLE
	huffman.py file has code for compressing and decompressing in Huffman
tests folder contains test scripts and test cases
	compress.py file is a small script which finds all txt files in tests folder and compresses them
	decompress.py file is a small script which finds all txt files in tests folder and decompresses them
	clean.py file is a small script which deletes all .h and .lulz files in tests folder
