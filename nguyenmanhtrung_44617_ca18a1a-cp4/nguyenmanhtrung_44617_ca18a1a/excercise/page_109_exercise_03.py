"""
Author: Nguyễn Manh Trung
Date: 16/10/2000
Problem:


Solution:
def caesarCipher(string, key):
encrypted string = ()
new_key = key % 26
for letter in string:
encrypted string.append(getNewLetter(letter, new_key))
return '.join(encrypted string)
def getNewletter(letter, key):
new_letter = ord(letter) + key return chr(new_letter) if new letter <= 122 else chr(96 + new_letter122)
print (caesarCipher('hell0'))

....
"""