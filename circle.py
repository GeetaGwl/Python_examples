import turtle

from random import randint

win=turtle.Screen()
t=turtle.Turtle()

win.title("my window")
win.bgcolor("black")
t.speed(10)

for i in range(10):
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    win.colormode(255)
    t.pencolor(r,g,b)
    t.circle(90)
    t.rt(36)

win.exitonclick()    