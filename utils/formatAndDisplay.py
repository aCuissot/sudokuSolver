import constantes


def formatLine(line):
    i = 0
    outLine = ""
    for char in line:
        if i % constantes.SIZEOFASQUARE == 0:
            outLine += '| '
        outLine += char + ' '
        i += 1
    return outLine[2:]


def createBlankLine():
    line = ""
    for i in range(int(constantes.SIZEOFASQUARE)):
        line += (int(constantes.SIZEOFASQUARE) * "--") + "+-"
    return line[:-2]


def formatedSudokuToString(sudoku):
    sudoku = sudoku.replace("0", " ")
    formated_sudoku = ""
    for i in range(constantes.SIZEOFALINE):
        formated_sudoku+=formatLine(sudoku[i * constantes.SIZEOFALINE:(i + 1) * constantes.SIZEOFALINE])
        formated_sudoku+='\n'
        if i % constantes.SIZEOFASQUARE == constantes.SIZEOFASQUARE - 1 and i != constantes.SIZEOFALINE - 1:
            formated_sudoku+=createBlankLine()
            formated_sudoku += '\n'
    return formated_sudoku


def displaySudoku(sudoku):
    print(formatedSudokuToString(sudoku))


sudoKu = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
displaySudoku(sudoKu)