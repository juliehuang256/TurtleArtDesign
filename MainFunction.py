import turtle
from DesignFunction import *
from random import *
turtle.colormode(255)
turtle.bgcolor('black')
bob = turtle.Turtle()
bob.speed(100)

for x in range(15):
    bob.circle(x)
    size = x + 5
    r = randint(0,255)
    g = randint(0,168)
    b = randint(168,255)
    c = (r,g,b)
    XP(bob,c,size)
    XD(bob,c,size)
    bob.right(180)
    bob.forward(160)


