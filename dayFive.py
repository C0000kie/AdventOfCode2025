import numpy as np

def getFreshIngredients(ranges, ingredients):
    currIngredientIdx = 0
    freshies = []
    for start, end in ranges:
        if currIngredientIdx == len(ingredients):
            break

        currIngredient = ingredients[currIngredientIdx]
        # currIngredient in range
        # not in range => 1. before the range => discard 2. after the range => move to next range

        while currIngredient <= end and currIngredientIdx < len(ingredients) - 1:
            # best Case it is in the range => add to list of fresh and check the next ingredients
            if isInRange([start, end], currIngredient):
                freshies.append(currIngredient)
                currIngredientIdx += 1
                currIngredient = ingredients[currIngredientIdx]
            else:
                # discard ingredient
                if currIngredient < start:
                    currIngredientIdx += 1
                    currIngredient = ingredients[currIngredientIdx]
                    continue

    return freshies

def isInRange(range, ingredient):
    return range[0] <= ingredient and ingredient <= range[1]


def insertIntoRange(ranges, inputRange):
    toInsertStart, toInsertEnd = inputRange[0], inputRange[1]

    for i in range(len(ranges)):
        currRangeStart = ranges[i][0]
        currRangeEnd = ranges[i][1]

        # if range fits in between two ranges => insert before
        if toInsertEnd < currRangeStart:
            ranges = insertAfterIdx(ranges, i - 1, [toInsertStart, toInsertEnd])
            return ranges
        # Fully in range => do nothing return
        if isInRange(ranges[i], toInsertStart) and isInRange(ranges[i], toInsertEnd):
            return ranges
        # new range entails old curr range =< replace
        if toInsertStart < currRangeStart and currRangeEnd < toInsertEnd:
            if isLeftMerger(ranges, i, toInsertStart):
                ranges = mergeLeft(ranges, i, currRangeEnd)
            if isRightMerger(ranges, i, toInsertEnd):
                ranges = mergeRight(ranges, i, currRangeStart)
            else:
                ranges[i] = [toInsertStart,toInsertEnd]
            return ranges
        # right overlap => adjust end
        if currRangeEnd < toInsertEnd and isInRange(ranges[i], toInsertStart):
            if isRightMerger(ranges, i, toInsertEnd):
                ranges = mergeRight(ranges, i, currRangeStart)
            else:
                ranges[i] = [currRangeStart, toInsertEnd]
            return ranges
        # left overlap => adjust start
        if toInsertStart < currRangeStart and isInRange(ranges[i], toInsertEnd):
            if isLeftMerger(ranges, i, toInsertStart):
                ranges = mergeLeft(ranges, i, currRangeEnd)
            else:
                ranges[i] = [toInsertStart, currRangeEnd]

            return ranges


    # if range is larger than all seen ranges
    ranges.append([toInsertStart, toInsertEnd])
    return ranges

def countRanges(ranges):
    total = 0
    for range in ranges:
        rangeStart = range[0]
        rangeEnd = range[1]
        diff = rangeEnd -  rangeStart
        total += diff + 1
    return total
def verifyRanges(ranges):
    for i, range in enumerate(ranges[1:], start=1):
        prevStart = ranges[i - 1][0]
        prevEnd = ranges[i - 1][1]
        currStart = range[0]
        currEnd = range[1]
        # curr start < curr end
        if currStart > currEnd:
            print("Range invalid")
            print("Curr Range" + str(range))
            return
        # prev start < curr start
        if prevStart >= currStart:
            print("Ordering Incorrect")
            print("i: " + str(i))
            print("Curr Range" + str(range))
            print("Prev Range" + str([prevStart,prevEnd]))
            return
        # is prev end < curr start
        if prevEnd >= currStart:
            print("Overlap detected")
            print("Curr Range" + str(range))
            print("Prev Range" + str([prevStart,prevEnd]))
            return

    print("Ranges look good")


def insertAfterIdx(inputList, idx, elt):
    previousSnip = inputList[:idx + 1]
    previousSnip.append(elt)
    previousSnip.extend(inputList[idx + 1:])
    return previousSnip

def isLeftMerger(ranges, currIdx, currStart):
    if currIdx != 0:
        return isInRange(ranges[currIdx - 1], currStart)
    return False

def mergeLeft(ranges, currIdx, currEnd):
    previousStart = ranges[currIdx - 1][0]
    newRange = [previousStart, currEnd]
    ranges[currIdx] = newRange
    del ranges[currIdx - 1]

    return ranges

def mergeRight(ranges, currIdx, currStart):
    nextEnd = ranges[currIdx + 1][1]
    newRange = [currStart, nextEnd]
    ranges[currIdx] = newRange

    del ranges[currIdx + 1]
    return ranges

def isRightMerger(ranges, currIdx, currEnd):
    if currIdx != len(ranges):
        return isInRange(ranges[currIdx + 1], currEnd)
    return False

def processInput(filePth):
    ranges = []
    # {startIDX: end}
    ingredients = []
    with open(filePth) as file:
        for line in file:
            currLine = line.rstrip()
            if currLine == "":
                continue
            if currLine.__contains__("-"):
                range = np.array([int(elt) for elt in currLine.split("-")])
                ranges = insertIntoRange(ranges, range)
            else:
                ingredients.append(int(currLine))
    sortedIngredients = np.sort(np.array(ingredients))
    freshIngredients = getFreshIngredients(ranges, sortedIngredients)
    verifyRanges(ranges)
    print("freshies "+ str(len(freshIngredients)))
    print("total: "+ str(countRanges(ranges)))
    print("ranges "+ str(ranges))
    #print(ingredients)
    return
