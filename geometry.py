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