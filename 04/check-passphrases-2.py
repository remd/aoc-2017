f = open ('input.txt', 'r')
valid = 0
for line in f:
    tokens = line.split()
    uniqueTokens = set([''.join(sorted(x)) for x in line.split()])
    # there would be less unique tokens if anagrams existed
    if len(tokens) == len(uniqueTokens):
        valid += 1

print valid
