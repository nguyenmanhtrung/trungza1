"""
Author: nguyen manh trung
Date: 24/10/2021
Problem:
    Restructure Newton’s method (Case Study 3.6) by decomposing it into three
    cooperating functions. The newton function can use either the recursive strategy
    of Project 1 or the iterative strategy of Case Study 3.6. The task of testing for the
    limit is assigned to a function named limitReached, whereas the task of computing a new
    approximation is assigned to a function named improveEstimate. Each
    function expects the relevant arguments and returns an appropriate value.
Solution:

    ....
"""
import math

TOLERANCE = 0.000001


def newton(x, estimate=1):
    """Return the square root of x """
    if limitReached(x, estimate):
        return estimate
    else:
        return newton(x, improveEstimate(x, estimate))


def limitReached(x, estimate):
    """Return True if the estimate is within
    the tolerance or false otherwise."""
    difference = abs(x - estimate ** 2)
    return  difference <= TOLERANCE


def improveEstimate(x, estimate):
    """Return True if the estimate is within
    the tolerance or false otherwise."""
    return (estimate + x / estimate) / 2


def main():
    """Allows the user to obtain square roots."""
    while True:
        x = input("Enter a positive number or enter/return to quit: ")
        if x == "":
            break
        x = float(x)
        print("The program is estimate is", newton(x))


main()