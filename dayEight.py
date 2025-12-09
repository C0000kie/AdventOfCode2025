import sys
import numpy as np
from scipy.spatial.distance import cdist
from collections import defaultdict

def findLastIdx(indices, numOfPoints, distMat):
    seenPoints = set([])
    for i, matIdx in enumerate(indices):
        x, y = np.unravel_index(matIdx, distMat.shape)
        seenPoints.add(x)
        seenPoints.add(y)

        if len(seenPoints) >= numOfPoints:
            return i

    return len(indices)


def processInput(pth, n):
    boxes = []
    with open(pth) as file:
        for line in file:
            currLine = line.rstrip()
            currBox = [float(strNum) for strNum in currLine.split(",")]
            boxes.append(currBox)

    distMat = cdist(boxes, boxes, metric='euclidean')

    # Part Two
    lowerTriIndices = np.tril_indices_from(distMat)
    distMat[lowerTriIndices] = sys.float_info.max
    numOfPoints = distMat.shape[0]
    distMat[range(numOfPoints), range(numOfPoints)] = sys.float_info.max

    sortedIndices = np.argsort(distMat, axis=None)
    lastIdx = findLastIdx(sortedIndices, numOfPoints, distMat)

    indices = [np.unravel_index(idx, distMat.shape) for idx in sortedIndices]#[:lastIdx]
    lastX = indices[lastIdx][0]
    lastY = indices[lastIdx][1]
    solutionPartTwo = boxes[lastX][0] * boxes[lastY][0]
    print("solutionPartTwo " + str(solutionPartTwo))

    # Part One
    circuitDict = {i: -1 for i in range(len(boxes))}
    numOfCircuits = 0
    for idx in indices[:n]:
        currX = idx[0]
        currY = idx[1]
        if circuitDict[currX] == circuitDict[currY] and circuitDict[currX] != -1:
            continue
        # both are not in a circuit == -1 create new one
        elif circuitDict[currX] == -1 and circuitDict[currY] == -1:
            circuitDict[currX] = numOfCircuits
            circuitDict[currY] = numOfCircuits
            numOfCircuits += 1
        # both are in a circuit
        elif circuitDict[currX] != -1 and circuitDict[currY] != -1:
            oldId = circuitDict[currY]
            newId = circuitDict[currX]
            for key, val in circuitDict.items():
                # checking for required value
                if val == oldId:
                    circuitDict[key] = newId
        # one is in a circuit, one is not 2 cases
        elif circuitDict[currX] != -1:
            circuitDict[currY] = circuitDict[currX]
        elif circuitDict[currY] != -1:
            circuitDict[currX] = circuitDict[currY]

    # get size of Circuits
    res = defaultdict(set)
    for key, val in circuitDict.items():
        if val == -1:
            continue
        res[val].add(key)

    solutionPartOne = np.prod(sorted([len(c) for c in res.values()])[-3:])
    print("solutionPartOne " + str(solutionPartOne))

    return solutionPartOne, solutionPartTwo

