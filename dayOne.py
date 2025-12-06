import numpy as np

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Part one
def handleTurn( currNum, rotationStr):
    rotationClicks = rotationStr[1:]

    if rotationStr.__contains__("R"):
        return handleRightTurn(currNum , int(rotationClicks))
    elif rotationStr.__contains__("L"):
        return handleLeftTurn(currNum, int(rotationClicks))

def handleRightTurn(currNumber, rotationClicks):
    currNumber += rotationClicks
    return currNumber % 100

def handleLeftTurn(currNumber, rotationClicks):
    rest = np.abs(rotationClicks) % 100
    newNum = (currNumber - rest)

    if (newNum < 0):
        return 100 + newNum
    else:
        return newNum


def countIncrease(filename):
    currDialNum = 50
    zeroCount = 0
    with open(filename) as file:
        for line in file:
            currLine = line.rstrip()
            currDialNum = handleTurn(currDialNum, currLine)
            print(currLine)
            print(currDialNum)
            if(currDialNum == 0):
                zeroCount += 1
    return zeroCount

#Part Two
def handleRightTurn2(currNumber, rotationClicks):

    if currNumber + rotationClicks < 100:
        currNumber += rotationClicks
        return 0, currNumber

    if (currNumber + rotationClicks) == 100:
        return 1, 0
    else:
        print("overflow")
        #add till we are at 100
        if (currNumber != 0):
            clicksAfterZero = rotationClicks - (100 - currNumber)
            zeroCount = 1
        else:
            clicksAfterZero = rotationClicks
            zeroCount = 0

        rest = clicksAfterZero % 100
        noRestDivident = (clicksAfterZero - rest)
        zeroCount += noRestDivident / 100
        #print("zeroCount" + str(zeroCount))
        return zeroCount, rest

def handleLeftTurn2(currNumber, rotationClicks):
    # check if rotationClicks is larger than currNumber => we would have to pass 0 at least once
    # if rotationsClick is smaller => easy peasy only single sub and 0
    # if rotationsClick=currNumber? => return 1 and ß

    # It fits without rest
    if(currNumber - rotationClicks > 0 ):
        currNumber -= rotationClicks
        return 0, currNumber
    # we hit 0 exactly
    if currNumber - rotationClicks == 0:
        return 1, 0
    else:
        print("underflow")
        # sub until we are at 0
        if currNumber != 0:
            clicksAfterZero = rotationClicks - currNumber
            zeroCount = 1
        else:
            clicksAfterZero = rotationClicks
            zeroCount = 0

        rest = clicksAfterZero % 100
        noRestDivident = (clicksAfterZero - rest)
        zeroCount += noRestDivident / 100
        #print("zeroCount" + str(zeroCount))

        return zeroCount, (100 - rest) % 100



def handleTurn2( currNum, rotationStr):
    rotationClicks = rotationStr[1:]

    if rotationStr.__contains__("R"):
        return handleRightTurn2(currNum , int(rotationClicks))
    elif rotationStr.__contains__("L"):
        return handleLeftTurn2(currNum, int(rotationClicks))

def countIncrease2(filename):
    currDialNum = 50
    zeroCount = 0
    with open(filename) as file:
        for line in file:
            currLine = line.rstrip()
            currZeroCount, currDialNum = handleTurn2(currDialNum, currLine)
            zeroCount += currZeroCount
            print("The dial is rotated "+ str(currLine) + " to point at " + str(currDialNum))
            print("zeroPasses " + str(currZeroCount))
    return zeroCount
