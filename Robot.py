import random

n = []
x = 0
y = 0

def importarray(x):
    x.append(['#'] * 12)

    for i in range(10):
        x.append(['#'] + [0] * 10 + ['x'])

    x.append(['#'] * 12)

def showarray(x):
    print()
    for j in range(1, 11):
        for i in range(1, 11):
            print(x[j][i], end=' ')
        print()

def genRobotPosition(n):
    global x,y
    x = random.randint(1,11)
    y = random.randint(1,11)
    n[x][y] = 'x'

def flood(x,z,y):
    for i in range(z-1, z+2):
        if x[i][y] != 'x':
            x[i][y] += 1
            if x[i][y] != '#':
                flood(n,x,y)
    for o in range(y-1, y+2):
        if x[z][o] != 'x':
            x[z][o] += 1
            if x[z][o] != '#':
                flood(n,x,y)

    # flood(n,i,o)
importarray(n)
genRobotPosition(n)
flood(n,x,y)
showarray(n)

