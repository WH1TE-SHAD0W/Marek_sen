n = input()
l = [ int(i) for i in n.split()]
print(l)
p = []
x = []
for i in range(len(n)):
    m = max(l)
    x.append(m)
    for i in range(len(n)):
        
    l.pop()
    print(m,l,x)
print(x) 