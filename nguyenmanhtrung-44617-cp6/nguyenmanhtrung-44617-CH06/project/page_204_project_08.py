"""
Author: nguyen manh trung
Date: 24/10/2021
Problem:

Solution:

    ....
"""
def printAll(seq):
    if seq:
        print(seq,"->",seq[0])
        printAll(seq[1:])

printAll(list(range(10)))