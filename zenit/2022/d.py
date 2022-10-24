p = []
for i in range(2):
    p.append(input())

q = []
for i in range(3):
    q.append(input())

for i in range(2):
    if p[i] >= q[0] + q[1] + q[2]:
        print('ano')
    for j in range(2):
        elif p[i] >= q[j] + q[j+1] :
