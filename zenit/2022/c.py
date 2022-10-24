n = int(input())

p = []
for i in range(n):
    p.append(input())

# if p[0][0] == '(' or p[0][0] == ')' :
#     if p[0][len(p)] == '(' or p[0][len(p)] == ')':
#         if p[len(p)][len(p[len(p)])] == '(' or p[len(p)][len(p[len(p)])] == ')':
#             if p[len(p)][0] == '(' or p[len(p)][0] == ')':
#                 print('dazdovka')

t= 0
for i in range(len(p)):
    t+=p[i].count('<')
    t+=p[i].count('>')

if t%2 == 0:
    print('dazdovka')
else:
    print('had')