import unittest
from division import dividir

class TestRestar(unittest.TestCase):
    def test_dividir(self):
        self.assertEqual(dividir(6,2), 3)
        self.assertEqual(dividir(10,5), 2)
        self.assertEqual(dividir(8, 4), 2)

if __name__ == "__main__":
    unittest.main()