"""
Author: nguyễn manh trung
Date: 16/10/2021
Problem:How would a column-major traversal of a grid work? Write a code segment that prints the positions
visited by a column-major traversal of a 2-by-3 grid.
Solution:
    A nested loop structure to traverse a grid consists of two loops, an outer one and an inner one.
Each loop has a different loop control variable. The outer loop iterates over one coordinate,
while the inner loop iterates over the other coordinate.

    ....
"""
width = 2
height = 3
for y in range(height):
    for x in range(width):
        print((x, y), end = " ")
    print()