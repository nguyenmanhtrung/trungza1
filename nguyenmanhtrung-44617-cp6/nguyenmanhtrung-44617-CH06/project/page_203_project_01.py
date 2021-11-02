"""
Author: nguyen manh trung
Date: 24/10/2021
Problem:
Package Newton’s method for approximating square roots (Case Study 3.6) in a
function named newton. This function expects the input number as an argument
and returns the estimate of its square root. The script should also include a main
function that allows the user to compute square roots of inputs until she presses
the enter/return key.
Solution:


    ....
"""
import math
#Initialize the tolerance
TOLERANCE = 0.000001
def newton(x):
    """Returns the square root of x."""
    # Perform the successive approximations
    estimate = 1.0
    while True:
        estimate = (estimate + x/ estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= TOLERANCE:
            break
    return estimate
def main():
    """ALlows the user to obtain square roots."""
    while True:
        #Receive the input number from the user
        x = input("Enter a positive number or enter/return to quit: ")
        if x == "":
           break
        x = float(x)
        # Output the result
        print("The program's estimate is", newton(x))
        print("Python's estimate is ", math.sqrt(x))
main()