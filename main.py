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

    currDay = 'dayEight'
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
    print(dayEight.processInput(filenameSmall, 10))
    print(dayEight.processInput(filename, 1000))
