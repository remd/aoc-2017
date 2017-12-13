f = open("input.txt", "r").readlines()[0]
skipSize = 0
i = 0
lengths = [int(x) for x in f.split(",")]
vals = [x for x in range(0,256)]

def getIndex(currentPosition, move):
    return (currentPosition + move) % len(vals)

def reverseOrder(begin, end):
    sublist = []
    if end >= len(vals):
        sublist = vals[begin:] + vals[:getIndex(end, 0)]
    else:
        sublist = vals[begin:end]
    j = begin
    for num in reversed(sublist):
        vals[getIndex(j, 0)] = num
        j += 1

for l in lengths:
    if l <= len(vals):
        reverseOrder(i, i + l)
        i = getIndex(i, l + skipSize)
        skipSize += 1

print "%s, %s" % (vals[0], vals[1])
print vals[0] * vals[1]

