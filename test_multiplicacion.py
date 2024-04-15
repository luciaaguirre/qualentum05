import unittest
from multiplicacion import multiplicar

class TestSumar(unittest.TestCase):
    def test_multiplicar(self):
        self.assertEqual(multiplicar(3,2), 6)
        self.assertEqual(multiplicar(2,1), 2)
        self.assertEqual(multiplicar(2, 5), 10)

if __name__ == "__main__":
    unittest.main()