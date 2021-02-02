import unittest
import operations

class TestOperations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(operations.addition(70, 2), 72)

    def test_minus(self):
        self.assertEqual(operations.minus(15, 15), 0)

    def test_multiplication(self):
        self.assertEqual(operations.multiplication(10, 10), 100)

    def test_division(self):
        self.assertEqual(operations.division(50, 2), 25)

if __name__ == '__main__':
    unittest.main()


