"""
Author: Nguyễn Manh Trung
Date: 24/09/2021

Problem:Write a script that decrypts a message coded by the method used in Project 6.

Solution:

    ....
"""
message = input("Enter the coded text: ")
decimal = 0
exponent = len(message) - 1
bString = ""
for digit in message:
    decimal = decimal + int(digit) * 2 ** exponent
    exponent = exponent - 1

print(bString)