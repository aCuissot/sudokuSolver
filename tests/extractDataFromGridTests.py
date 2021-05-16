import unittest
from utils.extractDataFromGrid import *


class MyTestCase(unittest.TestCase):
    def test_missingNumbersInEntity(self):
        self.assertEqual(['1', '5', '6', '9'], missingNumbersInEntity("784003002"))
        self.assertEqual(['1', '2', '3', '4', '5', '6', '7', '8', '9'], missingNumbersInEntity("000000000"))
        self.assertEqual([], missingNumbersInEntity("123456789"))
        self.assertEqual(['5'], missingNumbersInEntity("123406789"))

    def test_getSquareConnectedRawsAndColumns(self):
        self.assertEqual([0, 1, 2], getSquareConnectedRawsAndColumns(1)[0])
        self.assertEqual([3, 4, 5], getSquareConnectedRawsAndColumns(1)[1])
        self.assertEqual([3, 4, 5], getSquareConnectedRawsAndColumns(5)[0])
        self.assertEqual([6, 7, 8], getSquareConnectedRawsAndColumns(5)[1])
        self.assertEqual([6, 7, 8], getSquareConnectedRawsAndColumns(8)[0])
        self.assertEqual([6, 7, 8], getSquareConnectedRawsAndColumns(8)[1])
        self.assertEqual([0, 1, 2], getSquareConnectedRawsAndColumns(0)[0])
        self.assertEqual([0, 1, 2], getSquareConnectedRawsAndColumns(0)[1])


if __name__ == '__main__':
    unittest.main()
