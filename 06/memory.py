def checksum(memory):
    return "".join([str(mem) for mem in memory])

def getIndexOfMaxBank(memory):
    largest = 0
    for num in memory:
        if num > largest:
            largest = num
    return memory.index(largest)

def reallocate(memory, i):
    num = memory[i]
    memory[i] = 0
    while num > 0:
        i += 1
        if i == len(memory):
            i = 0
        memory[i] = memory[i] + 1
        num -= 1

f = open("input.txt", "r")
memory = [int(num) for num in f.read().split()]
count = 0
checksums = dict()
while True:
    chk = checksum(memory)
    if chk in checksums:
        break
    else:
        checksums[chk] = 1
        reallocate(memory, getIndexOfMaxBank(memory))
    count += 1

print count
