import unittest
from array import calculate_average

class TestArr(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3.0)

    def test_single_element(self):
        self.assertEqual(calculate_average([10]), 10)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_average([])

    def test_precision(self):
        self.assertAlmostEqual(calculate_average([1.1, 2.2, 3.3]), 2.2, places=5)


if __name__ == '__main__':
    unittest.main()
