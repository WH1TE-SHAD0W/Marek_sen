t = int(input())
n = int(input())

p = []
for i in range(n):
    p.append(input())

q = []
for i in range (n):
    q.append(p[i].split(' '))

w = []
for i in range(n):
    # for j in range(len(q)):
    w.append(q[i][0]+q[i][1])

print(q)
r=[]
i=0
# while i <= len(q):
#     for j in range(2):
#         print(i,w,'__',q)
#         for o in range(len(q)):
#             if q[i][j] in q[o+1]:
#                 q[i]=(q[i]+q[o+1])
#                 q.pop(i+1)
#                 i+=1
#
#     i+=1
l=''
for i in range(n-1):
    for j in range(2):
        for o in range(n):
            pass
        if w[i+1] .__contains__(w[i][j]):
            l+=w[i+1]+w[i]
print(q,w)

