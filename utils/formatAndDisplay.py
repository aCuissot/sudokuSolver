import constantes


def formatLine(line):
    """

    :param line: a sudoku line string
    :return: the line formated as it will be displayed
    """
    i = 0
    outLine = ""
    for char in line:
        if i % constantes.SIZEOFASQUARE == 0:
            outLine += '| '
        outLine += char + ' '
        i += 1
    return outLine[2:]


def createBlankLine():
    """

    :return: create the horizontal lines to make the grid easier to visualise when displayed
    """
    line = ""
    for i in range(int(constantes.SIZEOFASQUARE)):
        line += (int(constantes.SIZEOFASQUARE) * "--") + "+-"
    return line[:-2]


def formatedSudokuToString(sudoku):
    """
    create the sudoku string as the sudoku have to be displayed
    :param sudoku: the sudoku string
    :return: a sudoku string ready to be display (with grid)
    """
    sudoku = sudoku.replace("0", " ")
    formated_sudoku = ""
    for i in range(constantes.SIZEOFALINE):
        formated_sudoku += formatLine(sudoku[i * constantes.SIZEOFALINE:(i + 1) * constantes.SIZEOFALINE])
        formated_sudoku += '\n'
        if i % constantes.SIZEOFASQUARE == constantes.SIZEOFASQUARE - 1 and i != constantes.SIZEOFALINE - 1:
            formated_sudoku += createBlankLine()
            formated_sudoku += '\n'
    return formated_sudoku


def displaySudoku(sudoku):
    """
    display a sudoku with the grid
    :param sudoku: the sudoku string
    """
    print(formatedSudokuToString(sudoku))
