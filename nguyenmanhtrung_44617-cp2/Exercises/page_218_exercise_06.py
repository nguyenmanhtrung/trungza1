"""
Author: nguyễn manh trung
Date: 16/10/2021
Problem: The Turtle class includes a method named circle. Import the Turtle class, run help(Turtle.circle),
and study the documentation. Then use this method to draw a filled circle and a half moon.
Solution:
    ....
"""
import turtle

# Initializing the turtle
t = turtle.Turtle()

r = 50
t.circle(r)

turtle.Screen()
turtle.bgcolor("magenta")

turtle.color("red")
turtle.begin_fill()
turtle.circle(130, 180)
turtle.end_fill()
turtle.hideturtle()
