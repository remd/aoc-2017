import copy

f = open("input.txt", "r")
maze = [int(line) for line in f]
count = 0
try:
    currentIndex = 0
    while True:
        x = maze[currentIndex]
        originIndex = copy.copy(currentIndex)
        currentIndex = currentIndex + x
        if x >= 3:
            maze[originIndex] = x - 1
        else:
            maze[originIndex] = x + 1
        count += 1
except IndexError:
    print count
