import tkinter

file = open('body.txt', 'r')
content = []
a = file.readline().strip()
# content = file.readline()
# lines = file.readlines()
while a != '':
    content.append(a)
    a = file.readline().strip()
file.close()

root = tkinter.Tk()

# create canvas
canvas = tkinter.Canvas(root, bg="white", height=850, width=850)

# obsah = content.split()
for i in range(len(content)):
    content[i] = content[i].split(";")

s = []
for i in range(len(content)):
    x = int(content[i][0])
    y = int(content[i][1])
    canvas.create_text(x*50,y*50,text=x)
    canvas.create_text(x*50+10,y*50,text=y)
    canvas.create_text(x*50,y*50+10,text=y+x)
    s.append(x + y)
m = 0

for i in range(len(content)):
    for j in range(2):
        print(int(content[i][j]))
        if int(content[i][j]) > m:
            m = i

# r = content.index(m)


n = s.index(min(s))
canvas.create_rectangle(int(content[n][0]) * 50, int(content[n][1]) * 50, int(content[m][0]) * 50,
                        int(content[m][1]) * 50, fill='black')

print(content, s, m, n)
# add to window and show
canvas.pack()
root.mainloop()
