import numpy as np
import collections

def splitBeamsCount(prevLine, currLine, pathCounts):
    newLine = set()
    numOfSplit = 0
    newPathCounts = collections.defaultdict(int)

    for idx in prevLine:

        if currLine[idx] == "^":
            if idx > 0:
                newLine.add(idx - 1)
                newPathCounts[idx - 1] = newPathCounts[idx - 1] + pathCounts[idx]
            if idx < len(currLine) - 1:
                newLine.add(idx + 1)
                newPathCounts[idx + 1] = newPathCounts[idx + 1] + pathCounts[idx]
            numOfSplit += 1
        else:
            newLine.add(idx)
            newPathCounts[idx] = newPathCounts[idx] + pathCounts[idx]
    return newLine, numOfSplit, newPathCounts

def countPaths(paths):
    count = 0
    for elt in paths.values():
        count += elt
    return count

def processInputPartOne(pth):
    numOfSplits = 0
    with open(pth) as file:
        startIdx = list(file.readline().rstrip()).index("S")
        prevLine = set([startIdx])
        curPathCount = {startIdx: 1 }

        for line in file:
            currLine = list(line.rstrip())
            prevLine, currNumOfSplits, curPathCount = splitBeamsCount(prevLine, currLine, curPathCount)
            numOfSplits += currNumOfSplits

    countTotal = countPaths(curPathCount)
    return numOfSplits, countTotal