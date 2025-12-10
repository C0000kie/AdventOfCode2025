import re

def parseLine(line):
    lightDiagram = [False if str == "." else True  for str in re.search("[\.\#]+", line).group()]
    buttons = [[ int(d) for d in bStr.split(",")] for bStr in re.findall("(?<=\()[\d\,]+", line)]
    joltRequirements = [ int(d) for d in  re.search("(?<=\{)[\d\,]+", line).group().split(",")]
    return lightDiagram, buttons, joltRequirements

def applyButtonScheme(lightDiagram, buttonScheme):
    lightDiagram = list(lightDiagram)
    for button in buttonScheme:
        lightDiagram[button] = not lightDiagram[button]
    return lightDiagram


def updatePossibleStates(possibleStates, allButtonSchemes):
    newDict = {}
    for currState in possibleStates.keys():
        prevPath = possibleStates[tuple(currState)]
        for idx, buttonScheme in enumerate(allButtonSchemes):
            resState = applyButtonScheme(currState, buttonScheme)
            # new state how to kep track of path
            if tuple(resState) not in possibleStates:
                newPath = prevPath.copy()
                newPath.append(idx)
                newDict[tuple(resState)] = newPath # find out why out paths are 5 long instead of only one
    return newDict | possibleStates

def findCombination(lightDiagram, buttons):
    offState = [False for light in lightDiagram]
    possibleStates = {tuple(offState): []}
    while not tuple(lightDiagram) in possibleStates.keys():
        possibleStates = updatePossibleStates(possibleStates, buttons)
    return possibleStates[tuple(lightDiagram)]

def processInput(filePth):
    total = 0

    with open(filePth) as file:
        for line in file:
            currLine = line.rstrip()
            lightDiagram, buttons, joltRequirements = parseLine(currLine)
            path = findCombination(lightDiagram, buttons)
            total += len(path)
    return total
