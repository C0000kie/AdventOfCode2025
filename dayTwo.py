import numpy as np
import re

def generateSequences(startId, endId):
    startNum = int(startId)
    endNum = int(endId)
    return range(startNum, endNum + 1)


def isIdValid(id):
    idStr = str(id)
    #odd Ids cant be invalid
    if(len(idStr) % 2 != 0):
        return True
    halfIndex = int(np.floor(len(idStr) / 2))
    #parse both in parallel
    for i in range(0,halfIndex):
        firstHalfNum = idStr[i]
        secondHalfNum = idStr[halfIndex + i]
        if firstHalfNum != secondHalfNum:
            return True
    print("invalidIdSpotted: " + idStr)
    return False

def isIdValidPartTwo(id):
    idStr = str(id)
    # slices could be anything between 0 and halfid
    halfIndex = int(np.floor(len(idStr) / 2))
    for sliceLen in range(1, halfIndex + 1):
        isRepetition = isARepetitionId(idStr, sliceLen)
        if (isRepetition):
            return False
    return True

def isARepetitionId(idStr, sliceLen):
    patternToMatch = idStr[0:sliceLen]
    #check if it even fits fully
    if len(idStr) % sliceLen != 0:
        return False
    #parse til the end
    numOfPossibleFits = int(len(idStr) / sliceLen)
    for i in range(1, numOfPossibleFits):
        matches = re.match(patternToMatch, idStr[i*sliceLen:(i+1)*sliceLen])
        if matches == None:
            return False
    return True





def checkSequence(start, end):
    invalidIdsCount = 0
    invalidIds = []
    ids = generateSequences(start, end)
    for id in ids:
        if not isIdValidPartTwo(id):
            invalidIdsCount += 1
            invalidIds.append(id)
    return invalidIdsCount, invalidIds

def parseIdRange(idRangeStr):
    splits = re.split("-", idRangeStr)
    return splits[0], splits[1]

def addIds(idsList):
    sum = 0
    for id in idsList:
        sum += id
    return sum

def parseInput(inputPth):
    totalCount = 0
    totalIds = []
    with open(inputPth) as file:
        for line in file:
            currLine = line.rstrip()
            ranges = re.split(",", currLine)
            for range in ranges:
                print("current Range: " + str(range))
                start, end = parseIdRange(range)
                invalidCount, invalidIds = checkSequence(start, end)
                print("invalidCount: " + str(invalidCount))
                totalCount += invalidCount
                totalIds.extend(invalidIds)
    sum = addIds(totalIds)
    return totalCount, sum