f = open("input.txt", "r").readlines()[0].strip()
skipSize = 0
i = 0
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

def toAscii(inStr):
    ret = []
    for char in inStr:
        ret.append(ord(char))
    return ret

def denseHash(sparseHash):
    denseHash = []
    for n in range(0, 16):
        val = 0
        block = sparseHash[:16]
        for bit in block:
            val = val ^ bit
        denseHash.append(val)
        sparseHash = sparseHash[16:]
    return denseHash

def hexString(denseHash):
    hexString = ""
    for n in denseHash:
        hexString += "%0.2x" % n
    return hexString

# convert input to ascii codes + standard suffix
lengths = toAscii(f) + [17, 31, 73, 47, 23]
for n in range(0, 64):
    for l in lengths:
        if l <= len(vals):
            reverseOrder(i, i + l)
            i = getIndex(i, l + skipSize)
        skipSize += 1

finalVal = hexString(denseHash(vals))
print finalVal

