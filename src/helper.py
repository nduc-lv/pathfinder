import xmltodict
import haversine
graphml = open("../data/map2.graphml", "+br")
xmldoc = xmltodict.parse(graphml, xml_attribs=True)

# node: list of {'@id': '11337806829', 'data': [{'@key': 'd3', '#text': '21.0287243'}, {'@key': 'd4', '#text': '105.8598932'}]}
# edge: list of {'@source': '11337806829', '@target': '11337806828', '@id': '0', 'data': [{'@key': 'd7', '#text': '1222445909'}, {'@key': 'd15', '#text': 'service'}, {'@key': 'd8', '#text': 'False'}, {'@key': 'd9', '#text': 'True'}, {'@key': 'd10', '#text': '66.57'}]}]

road = {"primary":0, "secondary":0, "tertiary":0, "unclassified":0, "residential": 0}

def getLatLon(OSMId):
    # get the location of a node with the given OSMId
    nodes = xmldoc["graphml"]["graph"]["node"]
    size = len(nodes)
    lat = ""
    lon = ""
    for i in range(size):
        node = nodes[i]
        if (node["@id"] == OSMId):
            data = node["data"]
            for datum in data:
                if datum["@key"] == "d4":
                    lat = datum["#text"] #string
                if datum["@key"] == "d5":
                    lon = datum["#text"] #string
                    break
            break
    return (float(lat), float(lon)) # return a pair of coordinates


def getOSMId(lat, lon):
    # return the OSMId of the node with the given lat and lon
    nodes = xmldoc["graphml"]["graph"]["node"]
    id = ""
    for node in nodes:
        for datum in node["data"]:
            if (datum["@key"] == "d4"):
                nodeLat = datum["#text"]
            if (datum["@key"] == "d5"):
                nodeLon = datum["#text"]
                break
        if (lat == float(nodeLat) and lon == float(nodeLon)):
            id = node["@id"]
            break
    return id


def getAdjacentNodes(OSMId):
    edges = xmldoc["graphml"]["graph"]["edge"]
    adjacentNodes = []
    length = 0
    isRoad = 0
    for edge in edges:
        if (edge["@source"] == OSMId):
            for datum in edge["data"]:
                if (datum["@key"] == "d10"):
                    length = float(datum["#text"]) #string
                    break
                elif (datum["@key"] == "d14"):
                    if (datum["#text"] in road):
                        isRoad = 1
            if (isRoad):
                adjacentNodes.append((edge["@target"], length))
    return adjacentNodes


def getHeuristic(point1, point2):
    return haversine.haversine(point1, point2)


def getPath(pathDict, endPoint):
    path = []
    point = endPoint
    while (pathDict[point] != None):
        point = pathDict[point]
        path.append(point)
    return path


def getResponse(pathDict, endPoint):
    response = []
    point = endPoint
    while (pathDict[point] != None):
        tmpDict = {}
        tmpDict["lat"] = point[0]
        tmpDict["lng"] = point[1]
        response.append(tmpDict)
        point = pathDict[point]
    response.append({"lat": point[0], "lng": point[1]})
    return response

def getResponseLeafLet(pathDict, endPoint):
    response = []
    point = endPoint
    while (pathDict[point] != None):
        tmpArray = []
        tmpArray.append(point[0])
        tmpArray.append(point[1])
        response.append(tmpArray)
        point = pathDict[point]
    response.append([point[0], point[1]])
    return response