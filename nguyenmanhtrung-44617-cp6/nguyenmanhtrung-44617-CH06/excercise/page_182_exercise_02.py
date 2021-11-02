"""
Author: nguyen manh trung
Date: 24/10/2021

Problem:
   In what way is a recursive design different from top-down design
Solution:
 A recursion should have a base case and an iteration case.

 The base case is the termination point at which the program should halt. If the base case is not perfect then the program never terminates and fall into infinite recursion.

 In case of infinite recursion, the python virtual machine runs out of memory and halts its execution indicating a “stack overflow error”

 The iteration case tells about how the function should be iterated to get the expected output.

 Recursion reduces the size of the code and makes the code look more elegant.
    ....
"""