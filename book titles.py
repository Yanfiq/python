file = open("/usercode/files/books.txt", "r")

#your code goes here
for line in file:
    line = line.rstrip("\n")
    print(line[0]+str(len(line)))

file.close()