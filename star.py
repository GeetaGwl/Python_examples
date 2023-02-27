import turtle
win=turtle.Screen()
t=turtle.Turtle()
win.title("Star")
win.bgcolor("black")

                  
t.speed(0)

for i in range(8):
    t.pencolor("red")
    t.fd(50)
    t.rt(90)
    t.pencolor("green")
    t.bk(50)
    t.lt(45)
win.screensize(canvwidth=10, canvheight=10)
win.exitonclick()    

