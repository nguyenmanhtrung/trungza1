"""
Author: Nguyễn Manh Trung
Date: 24/09/2021
"""
a = str(bin(int(input("enter the number: "))))[2:]
key = int(input("enter the key shift: "))
#1011
s = a
print(s)
for i in range(key):
    s = s[len(s)-1] + s[:len(s)-1]
print("=>> ", s)

a = str(bin(int(input("enter the number: "))))[2:]
key = int(input("enter the key shift: "))
#1011
s = a
print(s)
for i in range(key):
    s = s[1:len(s)] + s[0]
print("=>> ", s)
