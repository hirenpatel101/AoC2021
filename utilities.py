def ReadFileIntoList(filename):
    with open("test.txt") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]