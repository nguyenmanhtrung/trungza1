"""
Author: Nguyễn Manh Trung
Date: 24/09/2021

Problem:Write a script named dif.py. This script should prompt the user for the names
of two text files and compare the contents of the two files to see if they are the
same. If they are, the script should simply output "Yes". If they are not, the script
should output "No", followed by the first lines of each file that differ from each
other. The input loop should read and compare lines from each file. The loop
should break as soon as a pair of different lines is found

Solution:

    ....
"""
file1 = input("Nhập file 1: ")
file2 = input("Nhập file 2: ")

same = True  # check whether if files are not same

with open(file1, "r") as fp, open(file2, "r") as fp1:
    for line1, line2 in zip(fp, fp1):
        if line1 != line2:
            same = False
            print("No")
            print(line1)
            print(line2)
            break

if same:
    print("yes")