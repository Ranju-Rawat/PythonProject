

with open("test.txt", "r") as reader:
    content = reader.readline()
    reversed(content) #reverse the list
with open("test.txt", "w") as write:
    for line in reversed(content):
        write.write(line)
    print(write)