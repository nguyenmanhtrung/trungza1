"""
Author: nguyễn manh trung
Date: 16/10/2021
Problem:The size of an image is 1680 pixels by 1050 pixels. Assume that this image has been
sampled using the RGB color system and placed into a raw image file. What is the
minimum size of this file in megabytes? (Hint: There are 8 bits in a byte, 1024 bits in
a kilobyte, and 1000 kilobytes in a megabyte.)
Solution:
    ....
"""
def shrink(image, factor):
    """Builds and returns a new image which is smaller
    copy of the argument image, by the factor argument."""
    width = image.getWidth()
    height = image.getHeight()
    new = Image(width / factor, height / factor)
    oldY = 0
    newY = 0
    while oldY < height - factor:
        oldX = 0
        newX = 0
        while oldX < width - factor:
            oldP = image.getPixel(oldX, oldY)
            new.setPixel(newX, newY, oldP)
            oldX += factor
            newX += 1
        oldY += factor
        newY += 1
    return image
