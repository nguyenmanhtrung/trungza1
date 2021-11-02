"""
Author: Nguyễn mạnh trung
Date: 19/09/2021
Problem:   Assume that the variable teststring refers to a string. Write a loop that prints
each character in this string, followed by its ASCII value.
Solution:
"""
str = input("Nhập String : ")
for i in range(len(str)):
    print("giá trị ascii của ký tự %c = %d" % (str[i], ord(str[i])))