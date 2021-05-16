import unittest
from utils.gettersAndSetters import *


class GettersSettersTests(unittest.TestCase):
    def test_getRaws(self):
        sudoKu = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
        self.assertEqual('004300209', getRaw(sudoKu, 0))
        self.assertEqual('042910300', getRaw(sudoKu, 8))

    def test_getColumns(self):
        sudoKu = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
        self.assertEqual('090273080', getColumn(sudoKu, 5))
        self.assertEqual('300000059', getColumn(sudoKu, 3))

    def test_getSquares(self):
        sudoKu = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
        self.assertEqual('004005070', getSquare(sudoKu, 0))
        self.assertEqual('300009060', getSquare(sudoKu, 1))
        self.assertEqual('209001043', getSquare(sudoKu, 2))
        self.assertEqual('006190050', getSquare(sudoKu, 3))
        self.assertEqual('000508910', getSquare(sudoKu, 7))
        self.assertEqual('105690300', getSquare(sudoKu, 8))

    def test_setRaws(self):
        sudoKu = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
        sudoKu2 = setRaw(sudoKu, 0, '604300219')
        self.assertEqual('604300219005009001070060043006002087190007400050083000600000105003508690042910300', sudoKu2)
        sudoKu2 = setRaw(sudoKu, 4, '190007400')
        sudoKu2 = setRaw(sudoKu2, 8, '642915387')
        self.assertEqual('004300209005009001070060043006002087190007400050083000600000105003508690642915387', sudoKu2)

    def test_setColumns(self):
        sudoKu = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
        sudoKu2 = setColumn(sudoKu, 0, '604300219')
        self.assertEqual('604300209005009001470060043306002087090007400050083000200000105103508690942910300', sudoKu2)
        sudoKu2 = setColumn(sudoKu, 4, '190007400')
        sudoKu2 = setColumn(sudoKu2, 8, '642915387')
        self.assertEqual('004310206005099004070000042006002089190007401050073005600040103003508698042900307', sudoKu2)

    def test_setSquares(self):
        sudoKu = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
        sudoKu2 = setSquare(sudoKu, 0, '604300219')
        self.assertEqual('604300209300009001219060043006002087190007400050083000600000105003508690042910300', sudoKu2)
        sudoKu2 = setSquare(sudoKu, 4, '190007400')
        sudoKu2 = setSquare(sudoKu2, 8, '642915387')
        self.assertEqual('004300209005009001070060043006190087190007400050400000600000642003508915042910387', sudoKu2)


if __name__ == '__main__':
    unittest.main()
