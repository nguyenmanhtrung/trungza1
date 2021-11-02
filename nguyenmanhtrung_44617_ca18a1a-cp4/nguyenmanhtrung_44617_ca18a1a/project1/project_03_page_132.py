"""
Author: Nguyễn Manh Trung
Date: 24/09/2021
"""
def encrypt():
    with open("input.txt", "r") as f:
        text = f.read()
        import bai1 as bEncoding
        encoding = bEncoding.cipher_encrypt(text, key=int(input("Key: ")))
        with open("output.txt", "wb") as o:
            o.write(encoding)
        print("encoding: ",encoding)

def decrypt():
    with open("output.txt", "r") as f:
        text = f.read()
        import bai2 as bDecoding
        decoding = bDecoding.cipher_decrypt(text, key=int(input("Key: ")))
        with open("input.txt", "wb") as o:
            o.write(decoding)
        print("decoding: ",decoding)