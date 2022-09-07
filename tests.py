import unittest
from main import *

class TestMain(unittest.TestCase):

    def test_norm_squared(self):
        self.assertEqual(norm_squared(1, 1), 2, "Should be 2")
        self.assertEqual(norm_squared(2, 2), 8, "Should be 8")
        self.assertEqual(norm_squared(1, 2), 5, "Should be 5")


if __name__ == '__main__':
    unittest.main()