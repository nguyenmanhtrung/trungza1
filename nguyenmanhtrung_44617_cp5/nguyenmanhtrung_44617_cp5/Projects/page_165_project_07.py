"""
Author:Nguyễn Mạnh Trung
Date: 11/10/2021

Problem:
            Write a program that inputs a text file. The program should print the unique
words in the file in alphabetical order
Solution:
    ....
"""
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
words=[];
for line in fh:
    words += line.split()
words.sort()

print("The unique words in  alphabetical order are:")
for word in words:
    if word in lst:
            continue
    else:
            lst.append(word)
            print(word)


