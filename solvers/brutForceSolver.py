from itertools import permutations
from utils.gettersAndSetters import *
import constantes
from utils.extractDataFromGrid import *
from utils.formatAndDisplay import displaySudoku


def checkIfPartialGridColumnsGotError(sudoku):
    """
    here we check only columns and squares because with the way we fill raws, we cannot have error in a raw
    :param sudoku: the sudoku string
    :return: True if the grid don't have trivial error
             False if it have at least one
    """
    for i in range(constantes.SIZEOFALINE):
        currColumn = getColumn(sudoku, i)
        for j in range(1, constantes.SIZEOFALINE + 1):
            if currColumn.count(str(j)) > 1:
                return False
    for i in range(constantes.SIZEOFALINE):
        currSquare = getSquare(sudoku, i)
        for j in range(1, constantes.SIZEOFALINE + 1):
            if currSquare.count(str(j)) > 1:
                return False
    return True


# TODO: Check if we are faster and how faster we are with this function (maybe new operations cost is higher than the cost of operations no more done


def checkIfPartialGridColumnsGotErrorSmarter(sudoku, currRawNumber):
    """
    here we check only columns and some squares because with the way we fill raws, we cannot have error in a raw
    :param currRawNumber: the current raw filled
    :param sudoku: the sudoku string
    :return: True if the grid don't have trivial error
             False if it have at least one
    """
    for i in range(constantes.SIZEOFALINE):
        currColumn = getColumn(sudoku, i)
        for j in range(1, constantes.SIZEOFALINE + 1):
            if currColumn.count(str(j)) > 1:
                return False
    for i in range(constantes.SIZEOFASQUARE*int(currRawNumber/constantes.SIZEOFASQUARE), constantes.SIZEOFASQUARE*(int(currRawNumber/constantes.SIZEOFASQUARE)+1)):
        print(i)
        currSquare = getSquare(sudoku, i)
        for j in range(1, constantes.SIZEOFALINE + 1):
            if currSquare.count(str(j)) > 1:
                return False
    return True


def solveWithBrutForce(sudoku, i=0):
    """
    reccursively solve sudoku
    :param sudoku: sudoku string
    :param i: the current raw trying to
    :return: the solved sudoku
    """
    # case the previous change was not an error
    if not (i != 0 and not checkIfPartialGridColumnsGotError(sudoku)):
        # case we don't have errors (see previous if loop) and the grid is full => we have the right solution
        if i == constantes.SIZEOFALINE:
            print("solution:" + sudoku)
            return sudoku

        currRaw = getRaw(sudoku, i)
        missingNumbers = missingNumbersInEntity(currRaw)
        for permutation in permutations(missingNumbers):
            solveWithBrutForce(setPermutation(sudoku, i, permutation), i+1)
