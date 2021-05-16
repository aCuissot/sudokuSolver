import constantes


# Getters


def getLine(sudoku, lineNumber):
    """

    :param sudoku: the sudoku string
    :param lineNumber: the number of the line to return (starting to column 0)
    :return: the string containing the line asked
    """
    return sudoku[lineNumber * constantes.SIZEOFALINE: (lineNumber + 1) * constantes.SIZEOFALINE]


def getColumn(sudoku, columnNumber):
    """

    :param sudoku: the sudoku string
    :param columnNumber: the number of the column to return (starting to column 0)
    :return: the string containing the column asked
    """
    column = ""
    for i in range(constantes.SIZEOFALINE):
        column += sudoku[i * constantes.SIZEOFALINE + columnNumber]
    return column


def getSquare(sudoku, squareNumber):
    """
    square numbers are annotated as :
    012
    345
    678

    :param sudoku:  the sudoku string
    :param squareNumber: the number of the square to return (starting to column 0)
    :return: a string of the square
    """
    square = ""
    for i in range(constantes.SIZEOFASQUARE):
        square += sudoku[(i + constantes.SIZEOFASQUARE * (squareNumber // constantes.SIZEOFASQUARE)) * constantes.SIZEOFALINE + squareNumber % constantes.SIZEOFASQUARE * constantes.SIZEOFASQUARE: (i + constantes.SIZEOFASQUARE * (squareNumber // constantes.SIZEOFASQUARE)) * constantes.SIZEOFALINE + (squareNumber % constantes.SIZEOFASQUARE + 1) * constantes.SIZEOFASQUARE]
    return square


# Setters


def setLine(sudoku, lineNumber, newLine):
    """

    :param sudoku: the sudoku string
    :param lineNumber: the line to change number
    :param newLine: the new line value
    :return: the sudoku modified
    """
    return sudoku[:lineNumber * constantes.SIZEOFALINE] + newLine + sudoku[(lineNumber + 1) * constantes.SIZEOFALINE:]


def setColumn(sudoku, columnNumber, newColumn):
    """

    :param sudoku: the sudoku string
    :param columnNumber: the column to change number
    :param newColumn: the new column value
    :return: the sudoku modified
    """
    sudokuOut = sudoku[:columnNumber]
    for i in range(constantes.SIZEOFALINE - 1):
        sudokuOut += newColumn[i]
        sudokuOut += sudoku[i * constantes.SIZEOFALINE + columnNumber+1:(i+1) * constantes.SIZEOFALINE + columnNumber]
    return sudokuOut + newColumn[constantes.SIZEOFALINE-1] + sudoku[(constantes.SIZEOFALINE-1) * constantes.SIZEOFALINE + columnNumber +1:]


def setSquare(sudoku, squareNumber, newSquare):
    """

    :param sudoku: the sudoku string
    :param squareNumber: the square to change number
    :param newSquare: the new square value
    :return: the sudoku modified
    """
    sudokuOut = sudoku[:(constantes.SIZEOFASQUARE * (squareNumber // constantes.SIZEOFASQUARE)) * constantes.SIZEOFALINE + squareNumber % constantes.SIZEOFASQUARE * constantes.SIZEOFASQUARE]
    for i in range(constantes.SIZEOFASQUARE-1):
        sudokuOut += newSquare[i*constantes.SIZEOFASQUARE:(i+1)*constantes.SIZEOFASQUARE]
        sudokuOut += sudoku[(i + constantes.SIZEOFASQUARE * (squareNumber // constantes.SIZEOFASQUARE)) * constantes.SIZEOFALINE + (squareNumber % constantes.SIZEOFASQUARE + 1) * constantes.SIZEOFASQUARE: (i+1 + constantes.SIZEOFASQUARE * (squareNumber // constantes.SIZEOFASQUARE)) * constantes.SIZEOFALINE + squareNumber % constantes.SIZEOFASQUARE * constantes.SIZEOFASQUARE]
    return sudokuOut + newSquare[(constantes.SIZEOFASQUARE-1) * constantes.SIZEOFASQUARE:] + sudoku[(constantes.SIZEOFASQUARE - 1 + constantes.SIZEOFASQUARE * (squareNumber // constantes.SIZEOFASQUARE)) * constantes.SIZEOFALINE + (squareNumber % constantes.SIZEOFASQUARE + 1) * constantes.SIZEOFASQUARE:]


"""
sudoKu = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
detectionConversion.fromCSVConverter.displaySudoku(sudoKu)
for i in range(9):
    print(getSquare(sudoKu, i))
"""

