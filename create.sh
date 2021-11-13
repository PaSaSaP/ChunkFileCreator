#!/bin/bash

# Header:
# Current chunk (4), number of chunks (4), size of chunk (4), reserved (4)
# Chunk:
# Date (4), Time (4), HDOP (1), Velocity (3)

num_of_chunks=$((2*1024**2))
size_of_chunk=12
file_size=$((16+num_of_chunks*size_of_chunk))
file_name="t"
echo "Creating file named $file_name of size $file_size ($size_of_chunk * $num_of_chunks)"
BASEDIR=$(dirname "$0")
$BASEDIR/init_header.py -f $file_name -n $num_of_chunks -s $size_of_chunk

