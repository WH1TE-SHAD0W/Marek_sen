import tkinter
import random

# create canvas
root = tkinter.Tk()

# create canvas
canvas = tkinter.Canvas(root, bg="white", height=850, width=850)
canvas.pack()

color = ["red", "blue", "black", "grey", "green"]


def generate_text(x, y, angle, string: str, color):
    canvas.create_text(x, y, angle=angle, text=string, fill=color)


word = str(input())

angel = 360/(len(word)-1)

for i in range(len(word)):
    generate_text(100+i*20, 100, angel*i, word[i], random.choice(color))
root.mainloop()

