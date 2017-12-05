f = open ('input.txt', 'r')
valid = 0
for line in f:
    tokens = [str(x) for x in line.split()]
    tokenDict = dict()
    passphraseValid = True
    for token in tokens:
        if token in tokenDict:
            passphraseValid = False
            break
        else:
            tokenDict[token] = "lolwut"
    if passphraseValid:
        valid += 1

print valid
