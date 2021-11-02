"""
Author: Nguyễn Manh Trung
Date: 24/09/2021
Problem:Write a script named numberlines.py. This script creates a program listing from a
source program. This script should prompt the user for the names of two files. The
input filename could be the name of the script itself, but be careful to use a different
output filename! The script copies the lines of text from the input file to the output
file, numbering each line as it goes. The line numbers should be right-justified in
4 columns, so that the format of a line in the output file looks like this example:
1> This is the first line of text.

Solution:

    ....
"""
input_filename = input('Nhập file đầu vào: ')
output_filename = input('Nhập file đầu ra: ')

with open(input_filename, 'r') as f, open(output_filename, 'w') as w:
    number = 0
    for line in f:
        number += 1
        w.write('{:>4}> {}'.format(number, line))