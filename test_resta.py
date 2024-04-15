import unittest
from resta import restar

class TestRestar(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(restar(3,2), 1)
        self.assertEqual(restar(10,1), 9)
        self.assertEqual(restar(8, 1), 7)

if __name__ == "__main__":
    unittest.main()