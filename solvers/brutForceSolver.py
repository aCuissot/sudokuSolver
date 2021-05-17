from itertools import permutations
from utils.gettersAndSetters import *
import constantes
from utils.extractDataFromGrid import *


def checkIfPartialGridGotError(sudoku):
    """

    :param sudoku: the partial sudoku string, it need to be a complete number of raws
    :return: True if the grid don't have trivial error
             False if it have at least one
    """
    # check each raw
    numberOfRaws = int(len(sudoku) / constantes.SIZEOFALINE)
    for i in range(numberOfRaws):
        currRaw = getRaw(sudoku, i)
        for j in range(1, constantes.SIZEOFALINE + 1):
            if currRaw.count(str(j)) > 1:
                return False
    # check each partial column
    for i in range(constantes.SIZEOFALINE):
        currPartialColumn = getColumnPartial(sudoku, i)
        for j in range(1, constantes.SIZEOFALINE + 1):
            if currPartialColumn.count(str(j)) > 1:
                return False
    return True


def setPermutation(sudoku, rawNumber, permutation):
    raw = getRaw(sudoku, rawNumber)
    for i in permutation:
        raw.replace('0', i, 1)
    sudoku = setRaw(sudoku, rawNumber, raw)
    return sudoku


def solveWithBrutForce(sudoku, i=0):
    # case the previous change was an error
    if not checkIfPartialGridGotError(sudoku):
        return

    # case we don't have errors (see previous if loop) and the grid is full => we have the right solution
    if i == constantes.SIZEOFALINE:
        return sudoku

    currRaw = getRaw(sudoku, i)
    missingNumbers = missingNumbersInEntity(currRaw)
    for permutation in permutations(missingNumbers):
        print('i=' + str(i))
        print('permutation:' + ','.join(permutation))
        print(sudoku)
        solveWithBrutForce(setPermutation(sudoku, i, permutation), i+1)


sudoKu = "004300209005009001070060043006002087190007400050083000600000105003508690042910300"
solution = "864371259325849761971265843436192587198657432257483916689734125713528694542916378"

solved = solveWithBrutForce(sudoKu)
print(solved)
