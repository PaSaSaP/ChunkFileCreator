#!/usr/bin/env python3
import optparse

def from_bytes(v):
	return int.from_bytes(v, byteorder='little')

def main():
	parser = optparse.OptionParser()
	parser.add_option("-f", "--file", dest="filename", metavar="FILE")
	(options, args) = parser.parse_args()

	with open(options.filename, "rb") as f:
		current_chunk = from_bytes(f.read(4))
		num_of_chunks = from_bytes(f.read(4))
		chunk_size = from_bytes(f.read(4))
		reserved = from_bytes(f.read(4))
	print(F"current_chunk = {current_chunk}")
	print(F"num_of_chunks = {num_of_chunks}")
	print(F"chunk_size = {chunk_size}")
	print(F"reserved = {reserved}")

if __name__ == "__main__":
	main()

