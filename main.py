import dayNine
import dayOne
import dayTwo
import dayThree
import dayFour
import dayFive
import daySix
import daySeven
import dayEight
import newSol

import numpy as np
import os
import collections


if __name__ == '__main__':

    dirname = os.path.dirname(__file__)
    inputs = os.path.join(dirname, 'inputs')

    currDay = 'dayNine'
    filename = os.path.join(inputs, currDay + '\input.txt')
    filenameSmall = os.path.join(inputs, currDay + '\inputSmall.txt')

    # Day One
    """zeroCount = dayOne.countIncrease(filenameSmall)
    zeroCount = dayOne.countIncrease2(filename)
    print(zeroCount)"""

    # Day Two
    """totalCount, idSum = dayTwo.parseInput(filename)
    print("totalCount " + str(totalCount))
    print("idSum " + str(idSum))"""

    # Day Three
    """print(dayThree.processInput(filename))"""

    # Day four
    "print(dayFour.processInput(filename))"

    # Day five
    """print(dayFive.processInput(filenameSmall))
    print(dayFive.processInput(filename))
    """

    # Day Six
    """print(daySix.processInputPartOne(filename))
    print(daySix.processInputPartTwo(filename))"""

    # Day Seven
    """print(daySeven.processInputPartOne(filename))"""

    # Day Eight
    """print(dayEight.processInput(filenameSmall, 10))
    print(dayEight.processInput(filename, 1000))"""

    # Day Nine
    print(dayNine.processInput(filename))
    """pointA = [2,5]
    pointB = [11,1]
    pointA = [0, 1]
    pointB = [1, 0]

    allPoints = [[1,2], [500, 200]]
    print(dayNine.getOtherPoints(pointA, pointB))"""

    # 105974588 is too low
    #print(dayNine.isInBounds([1,2], allPoints, 'tr'))
    # first num is column and second num is row
    # 4781546175
    # 2286850234
    # 9284176
    # 4653414735 => too high
    # 4781546175 gt

