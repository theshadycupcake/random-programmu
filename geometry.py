import math, sys, time, turtle
from turtle import *
def draw_equilateral_triangle(x):
    t = turtle.Turtle()
    t.fd(x)
    t.lt(120)
    t.fd(x)
    t.lt(120)
    t.fd(x)
#simppeli tasasiuinen kolmio'
def draw_square(x):
    t = turtle.Turtle()
    t.fd(x)
    t.lt(90)
    t.fd(x)
    t.lt(90)
    t.fd(x)
    t.lt(90)
    t.fd(x)
    t.lt(90)
#vielä simppelimpi neliön piirto
angle = 30
def fractree(size, lvl):   
  
    if lvl > 0:
        colormode(255)
          
       
        pencolor(0, 255//lvl, 0)
          
        forward(size)
  
        right(angle)
 
        fractree(0.8 * size, lvl-1)
          
        pencolor(0, 255//lvl, 0)
          
        lt( 2 * angle )
  
        fractree(0.8 * size, lvl-1)
          
        pencolor(0, 255//lvl, 0)
          
        right(angle)
        forward(-size)
        #very much not my code for my brain is not big enough to think how to draw this

#this is actually my code and holy fuck it took long to make
def helloworld():
    t= turtle.Turtle()
    t.speed(10)
    win = turtle.Screen()
    win.bgcolor("red")
    t.pensize(4)

    #H
    t.penup()
    t.goto(-320, 0)
    t.pendown()
    t.left(90)
    t.forward(70)
    t.penup()
    t.goto(-320, 35)
    t.down()
    t.right(90)
    t.forward(50)
    t.penup()
    t.goto(-270, 70)
    t.pendown()
    t.right(90)
    t.forward(70)

    #E
    t.penup()
    t.goto(-260, 0)
    t.pendown()
    t.right(180)
    t.forward(70)
    t.right(90)
    t.forward(35)
    t.penup()
    t.goto(-260, 35)
    t.pendown()
    t.forward(35)
    t.penup()
    t.goto(-260, 0)
    t.pendown()
    t.forward(35)

    #L
    t.penup()
    t.goto(-210, 70)
    t.pendown()
    t.right(90)
    t.forward(70)  
    t.left(90)
    t.forward(35)

    #L
    t.penup()
    t.goto(-165, 70)
    t.pendown()
    t.right(90)
    t.forward(70)  
    t.left(90)
    t.forward(35)


    #O
    t.penup()
    t.goto(-90, 00)
    t.pendown()

    for i in range (25):
        t.left(15)
        t.forward(10)

    #W
    t.penup()
    t.goto(0, 70)
    t.pendown()     
    t.right(90)
    t.forward(70)
    t.left(150)
    t.forward(70)
    t.right(150)
    t.forward(70)
    t.left(150)
    t.forward(70)

    #O
    t.penup()
    t.goto(115, 00)
    t.pendown()
    t.right(90)
    for i in range (25):
        t.left(15)
        t.forward(10)

    #R
    t.penup()
    t.goto(170, 0)
    t.pendown()
    t.left(90)
    t.forward(70)
    t.right(25)
    for i in range(20):
        t.right(15)
        t.forward(5)
    t.right(180)
    t.forward(70)

    #L
    t.left(55)
    t.penup()
    t.goto(220, 70)
    t.pendown()
    t.right(90)
    t.forward(70)  
    t.left(90)
    t.forward(35)

    #D
    t.penup()
    t.goto(270,0)
    t.pendown()
    t.left(90)
    t.forward(70)
    t.right(90)
    for i in range (13):
        t.right(14)
        t.forward(9)
    turtle.done()