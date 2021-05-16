import pandas as pd
import constantes


def loadDataBase(datasetPath):
    """

    :param datasetPath: a path to the csv dataset to load
    :return: the sudoku database: 2 lists containing the unsolved and the solved sudoku
    """
    csvContent = pd.read_csv(datasetPath, header=None)
    sudokus = csvContent.values.tolist()[1:]
    sudokusUnsolved = list(list(zip(*sudokus))[0])
    sudokusSolved = list(list(zip(*sudokus))[0])
    return sudokusUnsolved, sudokusSolved


def printLine(line):
    i = 0
    outLine = ""
    for char in line:
        if i % constantes.SIZEOFASQUARE == 0:
            outLine += '| '
        outLine += char + ' '
        i += 1
    print(outLine[2:])


def printBlankLine():
    line = ""
    for i in range(int(constantes.SIZEOFASQUARE)):
        line += (int(constantes.SIZEOFASQUARE) * "--") + "+-"
    print(line[:-2])


def displaySudoku(sudoku):
    sudoku = sudoku.replace("0", " ")
    for i in range(constantes.SIZEOFALINE):
        printLine(sudoku[i * constantes.SIZEOFALINE:(i + 1) * constantes.SIZEOFALINE])
        if i % constantes.SIZEOFASQUARE == constantes.SIZEOFASQUARE - 1 and i != constantes.SIZEOFALINE - 1:
            printBlankLine()



# sudoKu = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
# displaySudoku(sudoKu)
