f = open("input.txt", "r")
pipes = {}
groupCount = 0

def findConnected(connected, pipes, pipeId):
    connected.add(pipeId)
    for connection in pipes[pipeId]:
        if connection not in connected:
            findConnected(connected, pipes, connection)
    return connected


for line in f:
    pipeId = int(line.split('<->')[0].strip())
    directConnections = line.split('<->')[1].strip().split(',')
    pipes[pipeId] = [int(x) for x in directConnections]

unchecked = pipes.keys()
for pipeId in pipes.keys():
    if pipeId in unchecked:
        connected = set()
        connected = findConnected(connected, pipes, pipeId)
        groupCount += 1
        for checkedConnection in connected:
            try:
                unchecked.remove(checkedConnection)
            except KeyError:
                pass

print groupCount
