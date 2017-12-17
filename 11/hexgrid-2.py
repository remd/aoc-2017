f = open("input.txt", "r").readlines()[0]
class Hex:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "%s, %s, %s" % (self.x, self.y, self.z)

    def step(self, direction):
        if direction == 'n':
            self.y += 1
            self.z -= 1
        elif direction == 'ne':
            self.x += 1
            self.z -= 1
        elif direction == 'nw':
            self.x -= 1
            self.y += 1
        elif direction == 'sw':
            self.x -= 1
            self.z += 1
        elif direction == 'se':
            self.x += 1
            self.y -= 1
        else: # direction is 's'
            self.y -= 1
            self.z += 1
        assert self.x + self.y + self.z == 0

def manhattan(a, b):
    return max(abs(a.x - b.x), abs(a.y - b.y), abs(a.z - b.z))

def findMaxDistance(steps):
    maxDistance = 0
    currentHex = Hex(0, 0, 0)
    for step in steps:
        currentHex.step(step)
        distance = manhattan(Hex(0, 0, 0), currentHex)
        if distance > maxDistance:
            maxDistance = distance
    return maxDistance

print findMaxDistance(f.split(','))

