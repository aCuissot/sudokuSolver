import unittest
import constantes
from solvers.brutForceSolver import *


class TestBrutForceSolver(unittest.TestCase):
    def test_checkIfPartialGridGotError(self):
        sudoKu = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
        self.assertTrue(checkIfPartialGridGotError(sudoKu, 9))
        sudoKu = '154367289235469781'
        self.assertFalse(checkIfPartialGridGotError(sudoKu, 3))
        sudoKu = '154367289235649871'
        self.assertTrue(checkIfPartialGridGotError(sudoKu, 3))
        """self.assertEqual(True, False)
        self.assertEqual(True, False)
        self.assertEqual(True, False)
        self.assertEqual(True, False)"""




if __name__ == '__main__':
    unittest.main()
