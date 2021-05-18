from conversion.fromCSVConverter import loadDataBase
from solvers.brutForceSolver import solveWithBrutForce
from utils.formatAndDisplay import displaySudoku


if __name__ == '__main__':
    unsolved, solved = loadDataBase('./dataset/sudoku.csv')
    print(unsolved[0])
    print(solved[0])
    sudokU = "027006380003102400060000010570020001000957000800010007050090040008704600049000170"
    solveWithBrutForce(sudokU)
    solutionCalculated="127546389983172456465389712574628931631957824892413567756891243218734695349265178"
    displaySudoku(solutionCalculated)