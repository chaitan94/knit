clean:
	rm -f *.pyc
	rm -f tests/*.rle tests/*.mtf tests/*.lulz

cleanall:
	make clean
	rm -R __pycache__
