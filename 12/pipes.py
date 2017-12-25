f = open("input.txt", "r")
pipes = {}
connected = set()

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

print len(findConnected(connected, pipes, 0))
