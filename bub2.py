n = input()
l = [ int(i) for i in n.split()]
print(l)
p = []
x = []
for i in range(len(n)-1):
    m = max(l)
    x.append(m)
    l.pop(i)
    print(m,l,x)
print(x)