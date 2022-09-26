import generate_canvas
import random

# from generate_canvas import createcanvas

# n = int(input())

# createcanvas(n)

x = []

x.append([9]*12)

for i in range(10):
    x.append([9] + [0] * 10 + [9])

x.append([9]*12)

for i in range(10):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    if x[a][b] != 'x':
        x[a][b] = 'x'
    else:
        i -= 1

for j in range(1,11):
    for i in range(1,11):
        if x[j][i] == 'x':
            pass
        else:
            for o in range(j-1,j+2):
                for u in range(i-1,i+2):
                    if x[o][u] == 'x':
                        x[j][i] += 1

for j in range(1,11):
    for i in range(1,11):
        print(x[j][i], end=' ')
    print()

