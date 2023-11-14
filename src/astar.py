import helper as help
import heapq as hq
import time
import numpy as np
# start and end are OSMId

def astar(start, end):
    parent = {} #parent[nodeLocation] = nodeLocation
    # a* point, distance, nodeId
    # a* point ~ apoint
    startLocation = help.getLatLon(start)
    endLocation = help.getLatLon(end)
    parent[startLocation] = None
    startToEnd = help.getHeuristic(startLocation, endLocation)
    opened = [(startToEnd, 0, start, startLocation)]
    closed = {start: startToEnd}
    hq.heapify(opened)
    s = time.time()
    while (len(opened) > 0):
        currNodeAPoint, distanceToCurrNode, currNodeId, currNodeLocation = opened[0]
        hq.heappop(opened)
        closed[currNodeId] = currNodeAPoint
        if (currNodeId == end):
            break
        adjacentNodes = help.getAdjacentNodes(currNodeId) # node = (nodeId, length)
        for node in adjacentNodes:
            nodeOSMId, nodeLength = node
            nodeLocation = help.getLatLon(nodeOSMId)
            heuristic = help.getHeuristic(nodeLocation, endLocation)
            distanceToNode = distanceToCurrNode + nodeLength
            nodeAPoint = distanceToNode + heuristic
            value = (nodeAPoint, distanceToNode, nodeOSMId, nodeLocation)
            if (nodeOSMId not in closed):
                parent[nodeLocation] = currNodeLocation
                opened.append(value)
        hq.heapify(opened)
    print("Time taken to find path(in second): "+str(time.time()-s))
    return parent

# print(help.getPath(astar("98011280", "8176641101"), "8176641101"))
# astar("98011280", "8176641101")





            

