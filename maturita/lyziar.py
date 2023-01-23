import tkinter
import random

# root = tkinter.Tk()


# create canvas
canvas = tkinter.Canvas(bg="white", height=850, width=850)
canvas.pack()


# create skier
def ski(x, y, tag):
    canvas.create_line(x, y, x + 50, y, tags=tag)
    canvas.create_line(x + 25, y, x + 25, y - 50, tags=tag)
    canvas.create_line(x + 10, y - 30, x + 40, y - 30, tags=tag)
    canvas.create_oval(x + 10, y - 80, x + 40, y - 50, tags=tag)


name = ["ski1", "ski2", "ski3"]

m = {"ski1": 0, "ski2": 0, "ski3": 0}
v = {"ski1": 0, "ski2": 0, "ski3": 0}


def create():
    canvas.delete("all")
    canvas.create_line(700, 0, 700, 800)
    for i in range(300, 600, 100):
        ski(0, i, random.choice(name))
    m = {"ski1": 0, "ski2": 0, "ski3": 0}
    v = {"ski1": 0, "ski2": 0, "ski3": 0}


create()


def run():
    while True:
        for i in name:
            rand = random.randint(20, 50)
            canvas.move(i, rand, 0)
            m[i] += rand
            if m[i] >= 650:
                v[i] += 1
                create()
                run()
                break

        canvas.after(60)
        canvas.update()


run()
