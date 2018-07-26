import unittest
from .context import example

class TestFunction(unittest.TestCase):

    def test_throws_with_a_lt_zero(self):
       with self.assertRaises(Exception):
           example.a_function(-1, 2.5)
           
    def test_adds_2_and_3(self):
        self.assertEqual(5, example.a_function(2, 3))

if __name__ == "__main__":
    unittest.main()
