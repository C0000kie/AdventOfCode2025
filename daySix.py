import numpy as np

def reduceArrays(inputOne, inputTwo, operators):
    solution = inputOne
    for i, currOp in enumerate(operators):
        if currOp == "+":
            solution[i] = solution[i] + inputTwo[i]
        elif currOp == "*":
            solution[i] = solution[i] * inputTwo[i]
        else:
            print("unknown Operator at: " + str(i))
    return solution

def combineLines(lineOne, lineTwo):
    return [lineOne[i] + lineTwo[i] for i  in range(len(lineOne))]

def reducePartTwo(input, operators):
    aggregateFuntion = lambda  a,b: np.add(a,b)
    total = 0
    currSolution = 0

    for i, operator in enumerate(operators):
        if operator == "+":
            total += currSolution
            aggregateFuntion = lambda  a,b: np.add(a,b)
            currSolution = float(input[i])
        elif operator == "*":
            total += currSolution
            aggregateFuntion = lambda  a,b: np.multiply(a,b)
            currSolution = float(input[i])
        elif not input[i].isspace():
            currNum = float(input[i])
            currSolution = aggregateFuntion(currSolution, currNum)

    total += currSolution
    return total

def prepareDigitInput(currLine, maxDigits):
    output = []
    rest = len(currLine) % maxDigits + 1
    for i in range(0, len(currLine) - rest, maxDigits + 1):
        currString = currLine[i:i + maxDigits]
        output.append(list(currString))
    return output

def processInputPartOne(pth):
    with open(pth) as file:
        #extract operators
        for line in file:
            pass
        operators = line.split()

    with open(pth) as file:
        firstLine = file.readline().rstrip()
        problemSolution = np.array([float(elt) for elt in firstLine.split()])
        for line in file:
            currLine = line.rstrip()
            if currLine.__contains__("+") or currLine.__contains__("*"):
                break
            currArray = np.array([float(elt) for elt in currLine.split()])
            problemSolution = reduceArrays(problemSolution, currArray, operators)
    return np.sum(problemSolution)


def processInputPartTwo(pth):
    with open(pth) as file:
        #extract operators
        for line in file:
            pass
        operators = list(line)

    with open(pth) as file:
        inputNums = list( file.readline())

        for line in file:
            if line.__contains__("+") or line.__contains__("*"):
                break
            currLine = line
            inputNums = combineLines(inputNums, list(currLine))
    return reducePartTwo(inputNums, operators)