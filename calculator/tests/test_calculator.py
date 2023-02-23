try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../../calculator'
            )
        )
    )
except:
    raise

import unittest
from calculator import sum_py


class TestCalculator(unittest.TestCase):
    def test_sum_5_and_5_return_10(self):
        self.assertEqual(sum_py(5, 5), 10)

    def test_sum_5_negative_and_5_return_0(self):
        self.assertEqual(sum_py(-5, 5), 0)

    def test_sum_multiple_entries(self):
        x_y_outputs = (
            (10, 10, 20),
            (5, 5, 10),
            (1.5, 1.5, 3.0),
            (-5, 5, 0),
            (100, 100, 200),
        )

        for x_y_output in x_y_outputs:
            with self.subTest(x_y_output=x_y_output):
                x, y, output = x_y_output
                self.assertEqual(sum_py(x, y), output)

    def test_sum_x_not_is_int_or_float_return_assertionerror(self):
        with self.assertRaises(AssertionError):
            sum_py('11', 0)

    def test_sum_y_not_is_or_float_return_assertionerror(self):
        with self.assertRaises(AssertionError):
            sum_py(0, '11')


if __name__ == "__main__":
    unittest.main(verbosity=2)
