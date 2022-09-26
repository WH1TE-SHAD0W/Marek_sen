import generate_canvas
import random
import tkinter
# from generate_canvas import createcanvas
root = tkinter.Tk()

# create canvas
canvas = tkinter.Canvas(root, bg="white", height=850, width=850)

for i in range(11):
    canvas.create_line(10, 10 + i * 80, 800, 10 + i * 80)
    canvas.create_line(10 + i * 80, 10, 10 + i * 80, 800)
# add to window and show
canvas.pack()

# n = int(input())

# createcanvas(n)

x = []

x.append([9] * 12)

for i in range(10):
    x.append([9] + [0] * 10 + [9])

x.append([9] * 12)

for i in range(10):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    if x[a][b] != 'x':
        x[a][b] = 'x'
    else:
        i -= 1

def rate(z, y):
    if x[z] [y] != 'x':
        for o in range(z - 1, z + 2):
            for u in range(y - 1, y + 2):
                if x[o][u] == 'x':
                    x[z][y] += 1


for j in range(1, 11):
    for i in range(1, 11):
        rate(j, i)

for j in range(1, 11):
    for i in range(1, 11):
        print(x[j][i], end=' ')
    print()
def flood(z,y):
    if x[z][y] == 0:
        for o in range(z - 1, z + 2):
            for u in range(y - 1, y + 2):
                if x[o][u] != 9:
                        canvas.create_text(80*o-40,80*u+-40,text=x[o][u])
        if x[z][y] == 0:
            x[z][y] = 9
            for o in range(z - 1, z + 2):
                for u in range(y - 1, y + 2):
                    if x[o][u] == 0:
                        flood(o,u)
    else:
        canvas.create_text(80 * z - 40, 80 * y + -40, text=x[z][y])

def klik(a):
    x=a.x//80+1
    y=a.y//80+1
    print(x,y)
    flood(x,y)

canvas.bind("<Button-1>", klik)




root.mainloop()