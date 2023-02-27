from turtle import *
from random import randint

t=Turtle()
speed(1000)
bgcolor("black")

i=1

while i<=1000:
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    colormode(255)
    pencolor(r,g,b)
    fd(i*2)
    
    lt(45)
    rt(90)
    i=i+1



t.screen.exitonclick()

