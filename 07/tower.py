class Node:
    def __init__(self, name, weight, nodesAbove):
        self.name = name
        self.weight = weight
        self.nodesAbove = nodesAbove

f = open("input.txt", "r")
nodes = []
for line in f:
    data = line.split()
    if len(data) > 2:
        nodesAbove = []
        for name in data[data.index('->'):]:
            if name[-1] == ',':
                nodesAbove.append(name[:-1])
            else:
                nodesAbove.append(name)
            
        nodes.append(Node(data[0], int(data[1][1:-1]), nodesAbove))

lowest = nodes[0].name
nodes = nodes[1:]
while True:
    lowestFound = True
    for node in nodes:
        if lowest in node.nodesAbove:
            lowest = node.name
            nodes.remove(node)
            lowestFound = False
            break
    if lowestFound:
        break

print lowest