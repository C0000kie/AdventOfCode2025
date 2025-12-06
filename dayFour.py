import numpy as np

#def checkSurrounding(input, x, y):
def applySumFilter(input, kernelSize):
    padding = int((kernelSize - 1 )/ 2)
    paddedInput = np.pad(input,(padding,padding),'constant',constant_values=0)
    #paddedInput = paddedInput.reshape((paddedInput.shape[0], paddedInput.shape[1], 1))

    #print(paddedInput)

    rows, cols = input.shape
    output = np.empty(input.shape)

    for i in range(padding,rows + padding):
        for j in range(padding, cols + padding):
            currVal = paddedInput[i,j]
            slice = paddedInput[i - padding:i + padding + 1, j - padding:j + padding + 1]
            #print(slice)
            kernelSum = np.sum(slice) - currVal
            output[i - padding, j - padding] = 1 if kernelSum < 4 and currVal == 1 else 0

    return output

def processMat(input):
    sumMat  = applySumFilter(input, 3)
    removedRollsMat = input - sumMat
    return np.sum(sumMat), removedRollsMat

def createRow(currLine):
    return [0 if elt == "." else 1 for elt in currLine]

def processInput(filePth):
    inputMat = []
    outputMat = []
    with open(filePth) as file:
        for line in file:
            currLine = line.rstrip()
            currRow = createRow(currLine)
            inputMat.append(currRow)

    total = 0
    inputMat = np.array(inputMat)
    currRollRemoved, newInput = processMat(inputMat)
    total += currRollRemoved

    while currRollRemoved > 0:
        currRollRemoved, newInput = processMat(newInput)
        total +=currRollRemoved

    return total
