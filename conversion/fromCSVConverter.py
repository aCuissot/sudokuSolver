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
    sudokusSolved = list(list(zip(*sudokus))[1])
    return sudokusUnsolved, sudokusSolved




# sudoKu = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
# displaySudoku(sudoKu)
