f = open ('input.txt', 'r')
checksum = 0
for line in f:
    smallest = None
    largest = None
    for num in line.split():
        if smallest is None and largest is None:
            smallest = int(num)
            largest = int(num)
            # init
            continue
        if int(num) < smallest:
            smallest = int(num)
        if int(num) > largest:
            largest = int(num)
    checksum += largest - smallest

print checksum

