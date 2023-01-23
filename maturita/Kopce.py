import tkinter
import random

root = tkinter.Tk()
hill = []
#
hill.append(0)
hill.append(800)
n = random.randint(400,800)
v = random.randint()
# hill.append(n)

# create canvas
canvas = tkinter.Canvas(root, bg="white", height=850, width=850)

for i in range(40):
    k = random.randint(1,15)
    hill.append(i*10)
    hill.append(n - i*10-k)
    l = (n - i*10-k)

for i in range(40):
    k = random.randint(1,15)
    hill.append(400+i*10)
    hill.append(l + i*10+k)
hill.append(800)
hill.append(800)
print(hill)
canvas.create_polygon(hill)
# add to window and show
canvas.pack()
root.mainloop()
