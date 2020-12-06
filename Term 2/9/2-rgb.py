import turtle
import random

turtle.colormode(255)
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
turtle.color((r, g, b))
turtle.begin_fill()
for i in range(4):
    turtle.forward(200)
    turtle.left(90)
turtle.end_fill()

turtle.done()