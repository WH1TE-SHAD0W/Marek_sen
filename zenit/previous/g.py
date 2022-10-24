t = int(input())


x = []
for i in range(t):
    x.append(input())


def dateTime(w):
    y=0
    uni = 0
    r=[]
    r = w.split(' ')
    r[0] = r[0].split('.')
    r[1] = r[1].split(':')



for i in range(t):
    p=x[i].count('.')
    if p == 3:
        dateTime(x[i])
    # else:
        # crdate(x[i])
