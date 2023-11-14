import haversine
dataset = open("../data/out4.txt", "r")
nodes = []
count = 0
for x in dataset:
    [lat, lon] = x.split()
    nodes.append((float(lat), float(lon)))
def getNearestPoint(lat, lon):
    location = ()
    curr = 999999999
    for node in nodes:
        point = (float(lat), float(lon))
        distance = haversine.haversine(node, point)
        if (distance == 0):
            return point
        if (distance < curr):
            location = node
            curr = distance
    return (str(location[0]),str(location[1]))
def getAllPoints():
    ans = []
    for x in nodes:
        lat, lon = x
        ans.append([lat, lon])
    return ans
        
    
    