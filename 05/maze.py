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
        maze[originIndex] = x + 1
        count += 1
except IndexError:
    print count
