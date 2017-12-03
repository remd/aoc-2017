f = open ('input.txt', 'r')
checksum = 0
for line in f:
    row = [int(x) for x in line.split()]
    result = 0
    for a in row:
        for b in row:
            if a != b and a % b == 0:
                result = a / b
                checksum += result
                break

print checksum

