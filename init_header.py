#!/usr/bin/env python3
import optparse

def main():
	parser = optparse.OptionParser()
	parser.add_option("-f", "--file", dest="filename", metavar="FILE")
	parser.add_option("-n", "--number-of-chunks", type="int", dest="num_of_chunks")
	parser.add_option("-s", "--chunk-size", type="int", dest="chunk_size")
	(options, args) = parser.parse_args()

	with open(options.filename, "wb") as f:
		f.seek(0)
		f.write((0).to_bytes(4, byteorder='little'))  # current chunk
		f.write(options.num_of_chunks.to_bytes(4, byteorder='little'))
		f.write(options.chunk_size.to_bytes(4, byteorder='little'))
		f.write((0).to_bytes(4, byteorder='little'))  # reserved

if __name__ == "__main__":
	main()

