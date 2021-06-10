import turtle as tr
def drawMaze(times=100, degree=90):
    for i in range(times):
        color = 1-i/times
        pen.color(color, color, color)
        pen.fd(i)
        pen.left(degree)
inputnumber1 = int(input("pleas enter times: "))
inputnumber2 = int(input("pleas enter degree: "))
pen =tr.Turtle()
pen.speed(0)
drawMaze(inputnumber1, inputnumber2)
tr.done()