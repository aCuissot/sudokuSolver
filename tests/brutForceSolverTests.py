import unittest
import constantes
from solvers.brutForceSolver import *


class TestBrutForceSolver(unittest.TestCase):
    def test_checkIfPartialGridGotError(self):
        sudoKu = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
        self.assertTrue(checkIfPartialGridColumnsGotError(sudoKu))
        sudoKu = '864371259325849761971265843436192587198656432257483916689734125713528694542916378'
        self.assertFalse(checkIfPartialGridColumnsGotError(sudoKu))
        sudoKu = '864371259325849761971265843436192587198657432257483916689734125713528694542916378'
        self.assertTrue(checkIfPartialGridColumnsGotError(sudoKu))

    def test_checkIfPartialGridColumnsGotErrorSmarter(self):
        sudoKu = '004300209005009001070060043006002087190007400050083000600000105003508690042910330'
        self.assertTrue(checkIfPartialGridColumnsGotErrorSmarter(sudoKu, 3))
        sudoKu = '004300209005009001070060043006002087190007400050083000600000105003508690042910330'
        self.assertFalse(checkIfPartialGridColumnsGotErrorSmarter(sudoKu, 8))
        sudoKu = '864371259325849761971265843436192587198656432257483916689734125713528694542916378'
        self.assertFalse(checkIfPartialGridColumnsGotErrorSmarter(sudoKu, 8))
        sudoKu = '864371259325849761971265843436192587198657432257483916689734125713528694542916378'
        self.assertTrue(checkIfPartialGridColumnsGotErrorSmarter(sudoKu, 8))





if __name__ == '__main__':
    unittest.main()
