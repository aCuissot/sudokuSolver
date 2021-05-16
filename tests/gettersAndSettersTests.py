import unittest
from utils.gettersAndSetters import *


class MyTestCase(unittest.TestCase):
    def test_getLines(self):
        sudoKu = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
        self.assertEqual(getLine(sudoKu, 0), '004300209')
        self.assertEqual(getLine(sudoKu, 8), '042910300')

    def test_getColumns(self):
        sudoKu = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
        self.assertEqual(getColumn(sudoKu, 5), '090273080')
        self.assertEqual(getColumn(sudoKu, 3), '300000059')

    def test_getSquares(self):
        sudoKu = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
        self.assertEqual(getSquare(sudoKu, 0), '004005070')
        self.assertEqual(getSquare(sudoKu, 1), '300009060')
        self.assertEqual(getSquare(sudoKu, 2), '209001043')
        self.assertEqual(getSquare(sudoKu, 3), '006190050')
        self.assertEqual(getSquare(sudoKu, 7), '000508910')
        self.assertEqual(getSquare(sudoKu, 8), '105690300')

    def test_setLines(self):
        sudoKu = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
        sudoKu2 = setLine(sudoKu, 0, '604300219')
        self.assertEqual(sudoKu2, '604300219005009001070060043006002087190007400050083000600000105003508690042910300')
        sudoKu2 = setLine(sudoKu, 4, '190007400')
        sudoKu2 = setLine(sudoKu2, 8, '642915387')
        self.assertEqual(sudoKu2, '004300209005009001070060043006002087190007400050083000600000105003508690642915387')

    def test_setColumns(self):
        sudoKu = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
        sudoKu2 = setColumn(sudoKu, 0, '604300219')
        self.assertEqual(sudoKu2, '604300209005009001470060043306002087090007400050083000200000105103508690942910300')
        sudoKu2 = setColumn(sudoKu, 4, '190007400')
        sudoKu2 = setColumn(sudoKu2, 8, '642915387')
        self.assertEqual(sudoKu2, '004310206005099004070000042006002089190007401050073005600040103003508698042900307')

if __name__ == '__main__':
    unittest.main()
