file = open("test.txt")
# Read all the lines from a txt file
line = file.readline()

while line != "":
    print(line)
    line = file.readline()

