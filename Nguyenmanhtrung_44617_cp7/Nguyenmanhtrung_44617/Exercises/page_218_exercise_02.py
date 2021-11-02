"""
Author: nguyễn manh trung
Date: 16/10/2021
Problem:What is object instantiation? What are the options at the programmer’s disposal during
this process?
Solution:
    Is object instantiation: Before you use some objects, like a Turtle object, you must create them. To be precise, you must create
an instance of the object’s class. The process of creating an object is called instantiation.
Option: In the programs you have seen so far in this book, Python automatically created objects such as
numbers,strings, and lists when it encountered them as literals. The programmer must explicitly instantiate
other classes of objects, including those that have no literals.
    ....
"""
from PIL import Image



def grayscale(img, value):
    pixels = img.load()
    new_img = Image.new(img.mode, img.size)
    pixels_new = new_img.load()
    for i in range(new_img.size[0]):
        for j in range(new_img.size[1]):
            r, b, g = pixels[i,j]
            pixels_new[i,j] = (r - value, b - value, g - value, 0)
    new_img.show()



def brightness(img, value):
    pixels = img.load()

    img_new = Image.new(img.mode, img.size)
    pixels_new = img_new.load()
    for i in range(img_new.size[0]):
        for j in range(img_new.size[1]):
            r, b, g = pixels[i,j]
            pixels_new[i,j] = (r + value, b + value, g + value, 255)
    img_new.show()

def colorFilter(img, lst):
    pixels = img.load()
    new_img = Image.new(img.mode, img.size)
    pixels_new = new_img.load()
    for i in range(new_img.size[0]):
        for j in range(new_img.size[1]):
            r, b, g = pixels[i,j]
            pixels_new[i,j] = (r + lst[0], b + lst[1], g + lst[2])
    new_img.show()


img = Image.open("img.jpg")
grayscale(img, 100)
brightness(img, 60)
colorFilter(img, (90, 0, 0))
