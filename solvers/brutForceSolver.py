from itertools import permutations
from utils.gettersAndSetters import *
import constantes
from utils.extractDataFromGrid import *


def checkIfPartialGridGotError(sudoku, numberOfRaws):
    """

    :param numberOfRaws: the number of raws completed ad so to check
    :param sudoku: the partial sudoku string, it need to be a complete number of raws
    :return: True if the grid don't have trivial error
             False if it have at least one
    """
    # check each raw
    for i in range(numberOfRaws):
        currRaw = getRaw(sudoku, i)
        for j in range(1, constantes.SIZEOFALINE + 1):
            if currRaw.count(str(j)) > 1:
                return False
    # check each partial column
    for i in range(constantes.SIZEOFALINE):
        currColumn = getColumn(sudoku, i)
        for j in range(1, constantes.SIZEOFALINE + 1):
            if currColumn.count(str(j)) > 1:
                return False
    return True


def checkMoreSmart(sudoku):
    """
    here we check only columns because with the way we fill raws, we cannot have error in a raw
    :param sudoku: the sudoku string
    :return: True if the grid don't have trivial error
             False if it have at least one
    """
    for i in range(constantes.SIZEOFALINE):
        currColumn = getColumn(sudoku, i)
        for j in range(1, constantes.SIZEOFALINE + 1):
            if currColumn.count(str(j)) > 1:
                return False
    return True


def solveWithBrutForce(sudoku, i=0):
    # case the previous change was an error
    if i != 0 and not checkMoreSmart(sudoku):
        return
    # case we don't have errors (see previous if loop) and the grid is full => we have the right solution
    if i == constantes.SIZEOFALINE:
        print("solution:" + sudoku)
        return sudoku

    currRaw = getRaw(sudoku, i)
    missingNumbers = missingNumbersInEntity(currRaw)
    for permutation in permutations(missingNumbers):
        #print('i=' + str(i))
        #print('permutation:' + ','.join(permutation))
        #print(sudoku)
        solveWithBrutForce(setPermutation(sudoku, i, permutation), i+1)


sudoKu = "004300209005009001070060043006002087190007400050083000600000105003508690042910300"
solution = "864371259325849761971265843436192587198657432257483916689734125713528694542916378"

solved = solveWithBrutForce(sudoKu)
print(solved)

