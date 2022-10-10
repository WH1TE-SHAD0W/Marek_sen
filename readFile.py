file = open('text.txt')
content = file.readlines()
for i in range(len(content)):
    print(content[i], end='')
file.close()