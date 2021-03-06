#!/usr/bin/env python3

# Documentation (docstring)
"""Reading from text files

Usage:
    ./<script.py> input_file

Where:
    input_file is the name of an input text file
"""

# Exercise
"""
GOAL:
    Learn to read from file and modify input

NOTE:
    Scripting is often about reading files, parsing and modifying the input,
    and writing the result to files. In this exercice, we learn a common
    pattern to read from files.
    
    Whenever you see <script.py>, use the actual name of the script instead.
    
TODO:
    1) Complete the code below to modify the lines read by adding a line number
    at the start of the line and then print the results.

    2) Fool around with the existing code a bit to be sure you understand it.

LEARN:
    Use this pattern whenever you need to read from files.

CONCLUSION:
    In the next exercice, we will write to a file.
"""

# Modules
import sys

# Parse user input
try:
    input_file = sys.argv[1]
except:
    print(__doc__)
    sys.exit(1)

line_number = 0
with open(input_file) as input_file_handle:
    for line in input_file_handle:
        line_number += 1
        new_line = f"{line_number} {line.strip()}"
        print(new_line)
