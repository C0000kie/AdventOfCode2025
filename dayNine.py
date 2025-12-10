import numpy as np
from scipy.spatial.distance import cdist

def isInBounds(point, allPoints, pointType):
    col, row = point
    if pointType == "tl":
        mask = [p[0] <= col and p[1] <= row for p in allPoints]
        allPoints = np.array(allPoints)
        largerPoints = allPoints[mask]
        return len(largerPoints) >= 1
    if pointType == "tr":
        mask = [p[0] >= col and p[1] <= row for p in allPoints]
        allPoints = np.array(allPoints)
        largerPoints = allPoints[mask]
        return len(largerPoints) >= 1
    if pointType == "bl":
        mask = [p[0] <= col and p[1] >= row for p in allPoints]
        allPoints = np.array(allPoints)
        largerPoints = allPoints[mask]
        return len(largerPoints) >= 1
    if pointType == "br":
        mask = [p[0] >= col and p[1] >= row for p in allPoints]
        allPoints = np.array(allPoints)
        largerPoints = allPoints[mask]
        return len(largerPoints) >= 1

def getOtherPoints(pointA, pointB):
    # pointA 'tl', pointB 'br'
    if (pointA[0] <= pointB[0] and pointA[1] <= pointB[1]):
        print("pointA 'tl', pointB 'br'")
        return {'tr': [pointB[0], pointA[1]], 'bl': [pointA[0], pointB[1]]}
    # pointA 'br', pointB 'tl'
    if (pointA[0] >= pointB[0] and pointA[1] >= pointB[1]):
        print("pointA 'br', pointB 'tl'")

        return {'bl': [pointB[0], pointA[1]], 'tr': [pointA[0], pointB[1]]}

    # pointA 'tr', pointB 'bl'
    if (pointA[0] <= pointB[0] and pointA[1] >= pointB[1]):
        print("pointA 'tr', pointB 'bl'")
        return {'tl': [pointA[0], pointB[1]], 'br': [pointB[0], pointA[1] ]}

    #pointA 'bl', pointB'tr'
    if (pointA[0] >= pointB[0] and pointA[1] <= pointB[1]):
        print("pointA 'bl', pointB'tr'")
        return {'br': [pointA[0], pointB[1]], 'tl': [pointB[0], pointA[1] ]}


def processInput(filePth):
    points = []
    with open(filePth) as file:
        for line in file:
            currLine = line.rstrip().split(",")
            points.append([int(currLine[0]), int(currLine[1])])
    points = np.array(points)

    distMat = cdist(points, points, metric='euclidean')
    idxOne, idxTwo = np.unravel_index(np.argmax(distMat), distMat.shape)

    pointOne = points[idxOne, :].copy()
    pointTwo = points[idxTwo, :].copy()

    print("pointOne " + str(pointOne))
    print("pointTwo " + str(pointTwo))
    pointDict = getOtherPoints(pointOne, pointTwo)
    print(pointDict)
    allPointsInBounds = True
    for k, v in pointDict.items():
        if not isInBounds(v, points, k):
            break

    sideOne = np.sqrt(np.square(pointOne[0] - pointTwo[0] )) + 1
    sideTwo = np.sqrt(np.square(pointOne[1]  - pointTwo[1] ))  + 1

    solutionPartOne = sideOne * sideTwo

    """#sort in descendingOrder
    sortedIndices = np.argsort(- distMat, axis=None)
    #x,y = np.unravel_index(sortedIndices[0], distMat.shape)
    numOfPoints = len(points)
    lastIdx =  int(numOfPoints * (numOfPoints -1) / 2)

    currMaxArea = -1
    currMaxIdx = 0
    for idx in sortedIndices:
        x, y = np.unravel_index(idx, distMat.shape)
        pointOne = points[x, :].copy()
        pointTwo = points[y, :].copy()
        print("pointOne " + str(pointOne))
        print("pointTwo " + str(pointTwo))
        pointDict = getOtherPoints(pointOne, pointTwo)
        if(pointDict == None):
            print("problemIDx" + str(idx))

        allPointsInBounds = True
        for k, v in pointDict.items():
            if not isInBounds(v, points, k):
                allPointsInBounds = False
                break
        if (allPointsInBounds):
            sideOne = np.sqrt(np.square(pointOne[0] - pointTwo[0])) + 1
            sideTwo = np.sqrt(np.square(pointOne[1] - pointTwo[1])) + 1
            if sideOne * sideTwo > currMaxArea:
                currMaxArea =  sideOne * sideTwo
                currMaxIdx = idx
    """
    return solutionPartOne
