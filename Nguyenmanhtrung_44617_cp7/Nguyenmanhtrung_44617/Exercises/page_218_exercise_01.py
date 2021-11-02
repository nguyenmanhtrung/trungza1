"""
Author: nguyễn manh trung
Date: 16/10/2021
Problem:Explain the importance of the interface of a class of objects
Solution:
    Graphics is the discipline that underlies the representation and display of geometric shapes
    in two- and three-dimensional space, as well as image processing. Python comes with a large array
    of resources that support graphics operations. However, these operations are complex and not for the faint
    of heart.
    ....
"""
from turtle import Turtle
import time


# def drawCircle(distance):
#     t = Turtle()
#     for i in range(120):
#         t.left(3)
#         t.forward(distance)


# distance = int(input())
# drawCircle(distance)




coordinates = [];
radius = int(input("radius: "))
for i in range(2):
    coordinates.append(int(input()))


t = Turtle()
t.up()
t.goto(coordinates[0],coordinates[1])
t.down()
radius = 100
time.sleep(10)
t.circle(radius)


perimeter = 2 * 3.14 * radius
print("perimeter :",perimeter)

