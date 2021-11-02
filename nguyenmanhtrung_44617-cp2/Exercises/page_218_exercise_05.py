"""
Author: nguyễn manh trung
Date: 16/10/2021
Problem: Turtle graphics windows do not automatically expand in size. What do you suppose happens
when a Turtle object attempts to move beyond a window boundary?
Solution:
    if range is none then draw whole circle. If the range is not a circle then an arc endpoint is the current
pen position. Draw arc in anti-clockwise direction if radius is positive, counter-clockwise. Finally
the turtle's direction changes with the range.
    ....
"""