import turtle
import random

turtle.bgcolor('black')
turtle.speed(1000)
for i in range(0, 1000):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle.colormode(255)
    turtle.pencolor(r, g ,b)
    turtle.forward(i)
    turtle.left(90.9)

turtle.done()