import turtle
from turtle import*

screen=turtle.Screen()
t=turtle.Turtle()
t.speed(15)

#initially penup()
t.penup()
t.goto(-400,250)
t.pendown()

#Creating orange and white rectangles

t.color("orange")
t.begin_fill()
t.forward(800)
t.right(90)
t.forward(167)
t.right(90)
t.forward(800)
t.end_fill()
t.left(90)
t.color("white")
t.forward(167)

#Creating green rectangle
t.color("green")
t.begin_fill()
t.forward(167)
t.left(90)
t.forward(800)
t.left(90)
t.forward(167)
t.end_fill()

#Creating Big blue circle
t.penup()
t.goto(70,0)
t.pendown()
t.color("navy")
t.begin_fill()
t.end_fill()

#Creating big white circle
t.penup()
t.goto(60,0)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(60)
t.end_fill()

#Creating 24 mini blue circles
t.penup()
t.goto(-57,-8)
t.pendown()
t.color("navy")
for i in range(24):
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.penup()
    t.forward(15)
    t.right(15)
    t.pendown()

#Creating small blue circle
t.penup()
t.goto(20,0)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()

#Creating 24 spokes
t.penup()
t.goto(0,0)
t.pendown()
t.pensize(2)
for i in range(24):
    t.forward(60)
    t.backward(60)
    t.left(15)

turtle.done()