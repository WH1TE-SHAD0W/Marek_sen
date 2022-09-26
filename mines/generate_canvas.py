import tkinter


def createcanvas(n):
    root = tkinter.Tk()

    # create canvas
    canvas = tkinter.Canvas(root, bg="white", height=850, width=850)

    for i in range(n):
        canvas.create_line(10, 10 + i * 80, 800, 10 + i * 80)
        canvas.create_line(10 + i * 80, 10, 10 + i * 80, 800)
    # add to window and show
    canvas.pack()
    root.mainloop()
