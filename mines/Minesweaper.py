import os
import subprocess
import sys

import generate_canvas
import random
import tkinter

# from generate_canvas import createcanvas
root = tkinter.Tk()

# create canvas
canvas = tkinter.Canvas(root, bg="cyan", height=850, width=850)

# for i in range(11):
# canvas.create_line(10, 10 + i * 80, 800, 10 + i * 80)
# canvas.create_line(10 + i * 80, 10, 10 + i * 80, 800)
# add to window and show
canvas.pack()

# n = int(input())

# createcanvas(n)


x = []


def importminearray():
    x.append([9] * 12)

    for i in range(10):
        x.append([9] + [0] * 10 + [9])

    x.append([9] * 12)



importminearray()


def generatemine(z, y):
    i = 0
    while i < 2:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        if a + 2 >= z >= a - 1 and b + 2 >= y >= b - 1:
            pass
        else:
            if x[a][b] != 'x':
                x[a][b] = 'x'
                i += 1


def rate(z, y):
    if x[z][y] != 'x':
        for o in range(z - 1, z + 2):
            for u in range(y - 1, y + 2):
                if x[o][u] == 'x':
                    x[z][y] += 1


def ratewhole():
    for j in range(1, 11):
        for i in range(1, 11):
            rate(j, i)


def show():
    print()
    for j in range(1, 11):
        for i in range(1, 11):
            print(x[j][i], end=' ')
        print()


def flood(z, y):
    if x[z][y] == 0:
        for o in range(z - 1, z + 2):
            for u in range(y - 1, y + 2):
                if x[o][u] != 9:
                    canvas.create_rectangle(o * 80, u * 80, o * 80 - 80, u * 80 - 80, fill='white', outline='')
                    if x[o][u] != 0:
                        canvas.create_text(80 * o - 40, 80 * u + -40, text=x[o][u])
                        x[o][u] = 9
        if x[z][y] == 0:
            x[z][y] = 9
            for o in range(z - 1, z + 2):
                for u in range(y - 1, y + 2):
                    if x[o][u] == 0:
                        flood(o, u)
    elif x[z][y] != 9:
        canvas.create_rectangle(z * 80, y * 80, z * 80 - 80, y * 80 - 80, fill='white', outline='')
        canvas.create_text(80 * z - 40, 80 * y + -40, text=x[z][y])


k = 0

m = 0
def towin(z, y):
    global k,m
    if x[z][y] == 'x':
        canvas.create_text(400, 400, text='You loose')
        k += 1
    for i in range(12):
        m += x[i].count(9)

n = 0


def klik(a):
    global k,canvas,x
    if k <= 0:
        r = a.x // 80 + 1
        q = a.y // 80 + 1
        global n
        if n == 0:
            generatemine(r, q)
            ratewhole()
        show()
        flood(r, q)
        towin(r, q)
        n += 1


    else:
        subprocess.call([sys.executable, os.path.realpath(__file__)] +
        sys.argv[1:])
        k -=1
        x = []
        importminearray()

def flag(x,y):
    canvas.create_polygon(x * 80 + 20, y * 80 + 40, x * 80 + 50, y * 80 + 60, x * 80 + 50, y * 80 + 20, outline='black')
    canvas.create_line(x * 80 + 46, y * 80 + 50, x * 80 + 46, y * 80 + 80, width='10')
def rightclick(b):
    global x
    if k <= 0:
        r = b.x // 80 +1
        q = b.y // 80+1
        if x[r][q] == 'x' and x[r][q] != 9:
            flag(r-1,q-1)
canvas.bind("<Button-1>", klik)
canvas.bind("<Button-3>", rightclick)
root.mainloop()
