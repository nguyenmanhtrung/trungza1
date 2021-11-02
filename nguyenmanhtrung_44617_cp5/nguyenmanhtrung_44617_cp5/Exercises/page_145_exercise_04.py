"""
Author:Nguyễn Mạnh Trung
Date: 11/10/2021

Problem:
            Write a loop that accumulates the sum of the numbers in a list named data.
Solution:
    ...
"""
NumList = []

Number = int(input("Please enter the Total Number of List Elements : "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

total = sum(NumList)

print("\n The Sum of All Element in this List is : ", total)