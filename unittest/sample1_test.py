import unittest
from sample1 import add

class Sample1Tests(unittest.TestCase):
    def test_sample_a(self):
        self.assertEqual(add(1,2), 3)

if __name__ == "__main__":
    unittest.main()

