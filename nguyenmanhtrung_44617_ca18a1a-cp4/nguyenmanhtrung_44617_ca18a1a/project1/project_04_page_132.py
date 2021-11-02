"""
Author: Nguyễn Manh Trung
Date: 24/09/2021
"""
def decToOct(dec):
    return oct(dec)

print(decToOct(42))

def octToDec(oct):
    return int(oct, 8)

print(octToDec('0o52'))