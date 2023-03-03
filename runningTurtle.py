import random
import turtle
from turtle import *

farby = ['green', 'blue', 'orange', 'red', 'black']

turtles = []
for farba in farby:
    ext = Turtle()
    ext.penup()
    ext.goto(random.randrange(-300,300),random.randrange(-300,300))
    ext.pencolor(farba)
    ext.pendown()
    turtles.append(ext)

while True:
    for index in range(len(turtles)):
        if index+1 < len(turtles):
            turtles[index].setheading(turtles[index].towards(turtles[index+1]))
            turtles[index].forward(distance(turtles[index+1])/100)
        else:
            turtles[index].setheading(turtles[index].towards(turtles[0]))
            turtles[index].forward(distance(turtles[0])/100)
        print(index)

