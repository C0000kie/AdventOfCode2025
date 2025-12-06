import numpy as np

def findLargestNums(batteryBank):
    #arg max with stable sorting algo
    sortedIdx = np.argsort(-np.array(batteryBank), kind='mergsort')
    maxIdx = sortedIdx[0]
    if maxIdx == len(batteryBank) - 1:
        num = batteryBank[sortedIdx[1]] * 10 + batteryBank[maxIdx]
        return num

    for i in sortedIdx[1:]:
        if i > maxIdx:
            num = batteryBank[maxIdx] * 10 + batteryBank[i]
            return num

def findLargestTwelve(batteryBank):
    remainingDigits = 11
    firstSlice = batteryBank[:-remainingDigits]
    lastNumIdx = np.argmax(firstSlice)
    number = [batteryBank[lastNumIdx]]
    idx = [lastNumIdx]

    for i in reversed(range(0, remainingDigits)):
        if i == 0:
            # list[x:-0] => list[x:0] = []
            currSlice = batteryBank[lastNumIdx + 1:]
        else:
            currSlice = batteryBank[lastNumIdx+1:-i]
        lastNumIdx = lastNumIdx + 1 + np.argmax(currSlice)
        idx.append(lastNumIdx)
        nextNum = batteryBank[lastNumIdx]
        number.append(nextNum)

    return int("".join(map(str, number))),idx

def visualizeNum(batteryBank, indices):
    formattedStr = ""
    for i, digit in enumerate(batteryBank):
        currDigit = str(digit)
        if i in indices:
            currDigit = "\x1B[31m" +  currDigit +  "\x1B[0m"
        formattedStr += currDigit
    return formattedStr

def parseBankStrToIntList(batteryBanksStr):
    return [int(jol) for jol in batteryBanksStr]

def processInput(filePth):
    totalJoltage = 0
    with open(filePth) as file:
        for line in file:
            currLine = line.rstrip()
            batteryBankNums = parseBankStrToIntList(currLine)
            """currMaxJoltage = findLargestNums(batteryBankNums)
            totalJoltage += currMaxJoltage
            """
            currMaxJoltage, indices = findLargestTwelve(batteryBankNums)
            totalJoltage += currMaxJoltage
            print(visualizeNum(batteryBankNums, indices))
            print("currMaxJoltage: " + str(currMaxJoltage))
    return totalJoltage

