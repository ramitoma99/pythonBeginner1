def writeFile():
    first = open("test.txt", 'w')
    for i in range (1,7):
        first.write(f"line{i}\n")

def readFile():
    second = open("test.txt", 'r')
    splitted = second.read().split("\n")
    for i in range(4):
        if i != 3:
            print(splitted[i])
    else:
        pass

writeFile()
readFile()

#DONE