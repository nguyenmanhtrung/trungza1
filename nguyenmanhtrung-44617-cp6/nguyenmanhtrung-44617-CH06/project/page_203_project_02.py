"""
Author: nguyen manh trung
Date: 24/10/2021
Problem:
    Convert Newton’s method for approximating square roots in Project 1 to a recursive function named newton. (Hint:
    The estimate of the square root should be
    passed as a second argument to the function.)
Solution:

    ....
"""
import math
# Initialize the tolerance
TOLERANCE = 0.000001


def newton(x, estimate):
    """Return the square root of x """
    difference = abs(x - estimate ** 2)
    if difference <= TOLERANCE:
        return estimate
    else:
        return newton(x, (estimate + x / estimate) / 2)


def main():

    """Allows the user to obtain square roots."""
    while True:
        x = input("Enter a positive number or enter/return to quit: ")
        if x == "":
            break
        x = float(x)
        # Output the result
        print("The program is estimate is", newton(x, 1))
        print("Python is estimate is    ", math.sqrt(x))
main()
