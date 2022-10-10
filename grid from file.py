import tkinter
# from generate_canvas import createcanvas
root = tkinter.Tk()

# create canvas
canvas = tkinter.Canvas(root, bg="white", height=400, width=400)

# for i in range(11):
# canvas.create_line(10, 10 + i * 80, 800, 10 + i * 80)
# canvas.create_line(10 + i * 80, 10, 10 + i * 80, 800)
# add to window and show
canvas.pack()
file = open('text.txt')
content = file.readlines()
for i in range (len(content)):
    for u in range(len(content[i])):
        if content[i][u] == '1':
            canvas.create_rectangle(u*30,i*30,u*30+30,i*30+30, fill='green', )
        elif content[i][u] == '0':
            canvas.create_rectangle(u*30,i*30,u*30+30,i*30+30, fill='blue', )
        print(content[i][u], end='')

print(content)
root.mainloop()
file.close()

