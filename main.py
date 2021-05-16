from conversion.fromCSVConverter import loadDataBase


if __name__ == '__main__':
    unsolved, solved = loadDataBase('./dataset/sudoku.csv')
    print(unsolved[0])
