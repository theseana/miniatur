import turtle
import random


turtle.speed(1500)
for i in range(500):
    turtle.penup()
    x_random = random.randint(-600, 600)
    y_random = random.randint(-400, 400) 
    turtle.goto(x_random, y_random)
    turtle.pendown()
    for i in range(4):
        turtle.forward(200)
        turtle.left(90)

turtle.done()