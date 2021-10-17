#!/usr/bin/env python3
import optparse

def main():
	parser = optparse.OptionParser()
	parser.add_option("-f", "--file", dest="filename", metavar="FILE")
	(options, args) = parser.parse_args()

	with open(options.filename, "rb") as f:
		current_chunk = int.from_bytes(f.read(4), byteorder='big')
		num_of_chunks = int.from_bytes(f.read(4), byteorder='big')
		chunk_size = int.from_bytes(f.read(4), byteorder='big')
		reserved = int.from_bytes(f.read(4), byteorder='big')
	print(F"current_chunk = {current_chunk}")
	print(F"num_of_chunks = {num_of_chunks}")
	print(F"chunk_size = {chunk_size}")
	print(F"reserved = {reserved}")

if __name__ == "__main__":
	main()

