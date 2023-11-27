import re

coordinates = re.findall("\d+\.\d+", "LINESTRING (105.841142 21.0276569, 105.8410704 21.0274805, 105.8409946 21.0272351, 105.8409884 21.0272016)")
pairOfCoordinates = []
for i in range(1, len(coordinates), 2):
    pairOfCoordinates.append((float(coordinates[i]), float(coordinates[i - 1])))
print(pairOfCoordinates)

def extractLineString(lineString):
    coordinates = re.findall("\d+\.\d+", lineString)
    pairOfCoordinates = []
    for i in range(1, len(coordinates), 2):
        pairOfCoordinates.append((float(coordinates[i]), float(coordinates[i - 1])))
    return pairOfCoordinates
