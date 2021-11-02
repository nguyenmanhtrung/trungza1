"""
Author: nguyen manh trung
Date: 24/10/2021

Problem:
   What is the lifetime of a variable? Give an example
Solution:
The time during which a variable retains its value is known as its lifetime. The value of a variable may change over
its lifetime, but it retains some value. When a variable loses scope, it no longer has a value.

When a procedure begins running, all variables are initialized. A numeric variable is initialized to zero,
a variable-length string is initialized to a zero-length string (""), and a fixed-length string is filled with the
character represented by the ASCII character code 0, or Chr( 0 ). Variant variables are initialized to Empty.
Each element of a user-defined type variable is initialized as if it were a separate variable.
    ....
"""