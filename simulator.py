#! /usr/bin/python
import sys

# TODO: import parser
from vector3k import VECTOR3K

def main():

    # Read assembled input program
    if len(sys.argv) < 2:
        print 'Input program required: ./simulator.py <program_file_name>'
        sys.exit()
    program = parse_program(sys.argv[1])
    for instruction in program:
        print instruction
    inst = VECTOR3K()
    # TODO: Execute each instruction in processor
main()
