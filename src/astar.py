import helper as help
import heapq as hq
import time
import numpy as np


def astar(start, end):
    # start: OSMId of the first point
    # end: OSMId of the second point
    # return a tuple of a dictionary to trace the final path and the shortest distance
    previous = {} 
    finalDistance = 0
    # a* grade = aGrade
    startLocation = help.getLatLon(start)
    endLocation = help.getLatLon(end)
    previous[start] = None
    startToEnd = help.getHeuristic(startLocation, endLocation)
    opened_list_values = {start: (startToEnd, 0)}
    opened = [(startToEnd, 0, start)]
    closed = {start: startToEnd}
    hq.heapify(opened)
    s = time.time()
    while (len(opened) > 0):
        currNodeAGrade, distanceToCurrNode, currNodeId = opened[0]
        hq.heappop(opened)
        closed[currNodeId] = currNodeAGrade
        if (currNodeId == end):
            finalDistance = distanceToCurrNode
            break
        adjacentNodes = help.getAdjacentNodes(currNodeId) # node = (nodeId, length)
        for node in adjacentNodes:
            neighborNodeOSMId, currNodeToNodeLength = node
            neighborNodeLocation = help.getLatLon(neighborNodeOSMId)
            heuristic = help.getHeuristic(neighborNodeLocation, endLocation)
            distanceToNeighborNode = distanceToCurrNode + currNodeToNodeLength
            aGrade = distanceToNeighborNode + heuristic
            value = (aGrade, distanceToNeighborNode, neighborNodeOSMId)
            if (neighborNodeOSMId not in closed):
                # Nếu nút hàng xóm chưa trong tập mở
                if (neighborNodeOSMId not in opened_list_values):
                    # thêm vào tập mở
                    opened_list_values[neighborNodeOSMId] = (aGrade, distanceToNeighborNode)
                    opened.append(value)
                    previous[neighborNodeOSMId] = currNodeId
                # Nếu nút hàng xóm đã có trong tập mở
                else:
                    # nếu A* Grade (giá trị hàm f) của nút hàng xóm vừa tính được mà nhỏ hơn A* grade của nó trong hàm mở
                    if opened_list_values[neighborNodeOSMId][0] > aGrade:
                        old_aGrade =opened_list_values[neighborNodeOSMId][0]
                        old_distance = opened_list_values[neighborNodeOSMId][1]
                        # Thay thế  ...
                        opened.remove((old_aGrade, old_distance, neighborNodeOSMId))
                        opened_list_values[neighborNodeOSMId] = (aGrade, distanceToCurrNode)
                        opened.append(value)
                        previous[neighborNodeOSMId] = currNodeId
        hq.heapify((opened))
    print("Time taken to find path(in second): "+str(time.time()-s))
    return (previous, finalDistance)






            

