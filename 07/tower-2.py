nodes = dict()

class Node:
    def __init__(self, name, weight, nodesAbove):
        self.name = name
        self.weight = weight
        self.nodesAbove = nodesAbove

def calculateTowerWeight(node):
    total = 0
    if node.nodesAbove:
        for name in node.nodesAbove:
            total += calculateTowerWeight(nodes[name])
    return node.weight + total

def checkWeights(node):
    tmp = dict()
    revTmp = dict()
    for name in node.nodesAbove:
        towerWeight = calculateTowerWeight(nodes[name])
        tmp[name] = towerWeight
        revTmp[towerWeight] = name
    chk = set(tmp.values())
    if len(chk) == 1:
        return node
    else:
        print chk
        print tmp
        return checkWeights(nodes[revTmp[sorted(chk)[-1]]])

f = open("input.txt", "r")
for line in f:
    data = line.split()
    if len(data) == 2:
        nodes[data[0]] = Node(data[0], int(data[1][1:-1]), None)
    else:
        nodesAbove = []
        for name in data[3:]:
            if name[-1] == ',':
                nodesAbove.append(name[:-1])
            else:
                nodesAbove.append(name)
        nodes[data[0]] = Node(data[0], int(data[1][1:-1]), nodesAbove)

# we know from part 1 the lowest node is gmcrj
lowest = nodes["gmcrj"]
found = checkWeights(lowest)
print found.name, found.weight